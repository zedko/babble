from __future__ import annotations
from typing import Union
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from sqlalchemy.exc import InvalidRequestError, StatementError

from babbler import db


class Message(db.Model):
    """
    Message that any User's app sends
    """
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    importance = db.Column(db.String, nullable=False)
    user_uuid = db.Column(UUID, db.ForeignKey('user.uuid'), nullable=False)

    def __str__(self):
        return f'{self.importance} --> Message {self.id} from {self.source} \n{self.message}'

    @staticmethod
    def create_message(source: str = None,
                       message: str = None,
                       importance: str = None,
                       user_uuid: Union[uuid.UUID, str] = None) -> Message:
        """
        Creates a Message and saves it in database
        All parameters must be filled
        """
        if isinstance(user_uuid, uuid.UUID):
            user_uuid = str(user_uuid)
        message = Message(source=source, message=message, importance=importance, user_uuid=user_uuid)
        try:
            db.session.add(message)
            db.session.commit()
            return message
        except (InvalidRequestError, StatementError):
            db.session.rollback()
