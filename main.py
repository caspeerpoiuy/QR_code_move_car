from flask import Flask, make_response, request
from lib.captcha.captcha import captcha
from flask_restful import Resource, Api
from util.DbOperation.redis_utils import OperationRedis

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def get(self):
        # TODO: need to return a login template
        return {'hello': 'world'}

    def post(self):
        # TODO:
        pass


class Verify(Resource):
    def get(self):
        # redis_instance = OperationRedis.get_redis()
        # _, code, image = captcha.gererate_pic()
        # redis_instance.set(uuid, code, 60)
        # response = make_response(image)
        # response.content_type = "img/png·"
        # return response
        # TODO：need arguments uuid
        pass

    def post(self):
        # TODO: need arguments uuid, code, mobile
        pass


class Register(Resource):
    def get(self):
        pass

    def post(self):
        pass

api.add_resource(Login, '/login/')
api.add_resource(Verify, '/verify/')
api.add_resource(Register, '/register/')

if __name__ == '__main__':
    app.run(debug=True)

