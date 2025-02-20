from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, DateTime, String
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(80), nullable=False)
    body = db.Column(String(500), nullable=False)
    created_at = db.Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'body': self.body,
            'created_at': self.created_at 
        }
