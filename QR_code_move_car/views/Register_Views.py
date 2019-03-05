import re

from flask import request
from flask_restful import Resource

from Settings.configuration import db
from models.users import User


class Register(Resource):
    @staticmethod
    def post():
        username = request.json.get("username")
        password = request.json.get("password")
        confirm_password = request.json.get("confirm_password")
        if not all([username, password, confirm_password]):
            return {"error":"not all data"}
        if password != confirm_password:
            return {"error":"not all password"}

        # result_name = re.compile(r"[\u4e00-\u9fa5]")
        # result_password = re.compile(r"^[a-zA-Z]\w{6,18}")
        if True:
            try:
                user = User(username, password)
                session = db.session()
                db.session.add(user)
                db.session.commit()
                return {"good":"guys"}
            except Exception as e:
                print(e)
        else:
            return {"error":"not all "}
