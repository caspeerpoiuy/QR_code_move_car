from datetime import datetime
from Settings.configuration import Config


class BaseModel(object):
    create_time = Config.db.Column(Config.db.Datetime, default=datetime.now())
    update_time = Config.db.Column(Config.db.Datetime, default=datetime.now())


class User(Config.db.Model, BaseModel):
    __tablename__ = 'users'
    id = Config.db.Column(Config.db.Integer, primary_key=True)
    username = Config.db.Column(Config.db.String(64), unique=True, nullable=False)
    email = Config.db.Column(Config.db.String(128), unique=True, nullable=False)
    password_hash = Config.db.Column(Config.db.String(64), nullable=False)
    mobile = Config.db.Column(Config.db.String(11), unique=True, nullable=False)
    plate_number = Config.db.Column(Config.db.String(64), unique=True, nullable=False)
    is_admin = Config.db.Column(Config.db.Boolean, default=False)


