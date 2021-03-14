from __future__ import annotations
from typing import Optional
from babbler import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model):
    """
    User. Owner of Messages
    """
    # pk
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # model params
    email = db.Column(db.String(120), index=True, unique=True)
    telegram_id = db.Column(db.Integer)
    slack_id = db.Column(db.String(64))
    # relations
    messages = db.relationship('Message', cascade="all,delete", backref='owner', lazy='dynamic')
    # class params
    _cache = {}

    def __repr__(self):
        return f'<User {self.__dict__}>'

    @staticmethod
    def _pop_from_cache(user: User = None, email: str = None) -> Optional[User]:
        """
        Deletes instance from User._cache. Pass one of two parameters.
        :param user: optional. User obj to delete from cache
        :param email: optional. User's email
        :return: None
        """
        key = user.email or email
        return User._cache.pop(key, default=None)

    @staticmethod
    def create_user(credentials: dict) -> User:
        """
        Adds a new User to database and cache
        :param credentials: Should contain User parameters. "email" key is required - others are optional.
        :return: User instance
        """
        user = User(**credentials)
        try:
            db.session.add(user)
            db.session.commit()
            User._cache[user.email] = user
        except Exception as e:
            print("ERROR with user creation", e)
            db.session.rollback()
        return user

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        """
        Try to get User by email from cache or from database
        :param email: User's email
        :return: either [User, None]
        """
        user = None
        try:
            user = User._cache[email]
        except KeyError:
            user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def delete_user_by_email(email: str) -> None:
        """
        Deletes User by email from database
        :param email: User's email
        :return: None
        """
        user = User.get_user_by_email(email)
        if user:
            db.session.delete(user)
            db.session.commit()
            User._pop_from_cache(user=user)
        else:
            raise ValueError(f"Cannot delete User. No user with email -> {email} <- found")

    def delete_self(self) -> None:
        """
        Deletes current instance from database
        :return: None
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
