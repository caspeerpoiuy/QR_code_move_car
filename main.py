import qrcode
from flask import Flask, make_response, request
from lib.captcha.captcha import captcha
from flask_restful import Resource, Api
from util.DbOperation.redis_utils import OperationRedis

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    # @staticmethod
    def get(self, id):
        # TODO: need to return a login template
        return {'hello': id}

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

@app.route("/qrcode/")
def generate_qrcode():
    # url forward
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('http:www.baidu.com')
    qr.make(fit=True)
    img = qr.make_image()
    img.save("123.png")
    return "hello"

class Register(Resource):
    def get(self):
        pass

    def post(self):
        pass

api.add_resource(Login, '/login/<id>')
api.add_resource(Verify, '/verify/')
api.add_resource(Register, '/register/')

if __name__ == '__main__':
    app.run(debug=True)

