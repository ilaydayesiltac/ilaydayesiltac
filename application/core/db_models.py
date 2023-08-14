#!/usr/bin/python3
from application import db

class DomainInfo(db.Model):
    __tablename__ = 'domain_info'
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String)
    status_code = db.Column(db.Integer)
    title = db.Column(db.String)
    content = db.Column(db.String)
    is_it_key = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean, default=True)
    extra_info = db.Column(db.JSON)

class Users (db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, index=True)
    password = db.Column(db.String)
