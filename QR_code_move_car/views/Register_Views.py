from flask import request
from flask_restful import Resource


class Register(Resource):
    @staticmethod
    def get():
        return {"a":"2"}

    def post(self):
        pass