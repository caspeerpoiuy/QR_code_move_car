import qrcode
from PIL import Image
from flask import Flask, make_response, request
from lib.captcha.captcha import captcha
from flask_restful import Resource, Api
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from util.DbOperation.redis_utils import OperationRedis

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    @staticmethod
    def get(id):
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


class Register(Resource):
    def get(self):
        pass

    def post(self):
        pass


class Apply_QrCode(Resource):
    def get(self):
        qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4)
        qr.add_data("right")
        qr.make(fit=True)
        img = qr.make_image(fill_color="red", back_color="white")
        img = img.convert("RGBA")
        icon = Image.open("1.png")
        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        img.save("123.png")


    def post(self):
        pass



api.add_resource(Login, '/login/<id>')
api.add_resource(Verify, '/verify/')
api.add_resource(Register, '/register/')
api.add_resource(Apply_QrCode, '/qrcode/')

if __name__ == '__main__':
    app.run(debug=True)

