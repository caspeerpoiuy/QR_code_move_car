import re
import json
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from constants import *
from Settings.configuration import db
from models.users import User


class Register(Resource):
    @staticmethod
    def post():
        username = request.json.get("username")
        print(username)
        password = request.json.get("password")
        confirm_password = request.json.get("confirm_password")
        if not all([username, password, confirm_password]):
            return json.dumps({NOT_ALL_DATA:NOT_ALL_DATA_CODE})
        if password != confirm_password:
            return json.dumps({PASSWORD_ERROR:PASSWORD_ERROR_CODE})
        result_name = re.compile(r"^[a-zA-Z0-9_]{3,16}$")
        if not result_name.match(username):
            return json.dumps({USERNAME_NOT_MATCH:USERNAME_NOT_MATCH_CODE})
        result_password = re.compile(r"^(?=.*\d)(?=.*[a-zA-Z])(?=.*[\W_]).{10,20}$")
        if result_password.match(password):
            return json.dumps({PASSWORD_NOT_MATCH:PASSWORD_NOT_MATCH_CODE})
        if User.query.filter_by(username=username).first():
            return json.dumps({USER_EXIST:USER_EXIST_CODE})
        try:
            password_hash = generate_password_hash(password)
            user = User(username, password_hash)
            session = db.session()
            session.add(user)
            session.commit()
            return {"good":"guys"}
        except Exception as e:
            print(e)

