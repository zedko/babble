from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from babbler import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String)
    message = db.Column(db.String)
    importance = db.Column(db.String)
    user_uuid = db.Column(UUID, db.ForeignKey('user.uuid'))

    def __repr__(self):
        return f'<Message {self.id} from {self.source}>'
