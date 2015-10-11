from datetime import datetime
from flask.ext.bcrypt import Bcrypt
from .base import db, SessionMixin

class Streamer(db.Model, SessionMixin):
    id        = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id   = db.Column(db.Integer, nullable=False, unique=True, index=True)
    status    = db.Column(db.String(10), nullable=False, default='close')
    cover     = db.Column(db.Text)
    channel   = db.Column(db.String(64))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.user_id

    def __repr__(self):
        return '<Streamer: %s>' % self.id
