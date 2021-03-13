from babbler import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), index=True, unique=True)
    telegram_id = db.Column(db.Integer, unique=True)
    slack_id = db.Column(db.String(64), unique=True)
    messages = db.relationship('Message', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.email}>'
