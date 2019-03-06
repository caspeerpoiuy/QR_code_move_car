from datetime import datetime
from Settings.configuration import db


class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())


class User(db.Model, BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    mobile = db.Column(db.String(11), unique=True)
    plate_number = db.Column(db.String(64), unique=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = password
