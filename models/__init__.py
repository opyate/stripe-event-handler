from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import JSONB

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    "A Stripe event."

    __tablename__ = 'events'

    id = db.Column('id', db.Integer(), primary_key=True)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
    event_json = db.Column('event_json', JSONB, nullable=False)


    def __init__(self, event_json):
        self.event_json = event_json
