#!/usr/bin/python3
import uuid

from sqlalchemy.dialects.postgresql import JSONB

from application import db


class Link(db.Model):
    __name__ = "link"
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String)
    key = db.Column(db.String, unique=True)
    private_key = db.Column(db.String, unique=True, default=str(uuid.uuid4()))
    counter = db.Column(db.Integer)
    extra_information = db.Column(JSONB)
    # [
    #  {
    #    IP_address = db.Column(db.String)
    #    browser = db.Column(db.String)
    #    operatingSystem = db.Column(db.String)
    #    device = db.Column(db.String)
    #  }
    # ]
