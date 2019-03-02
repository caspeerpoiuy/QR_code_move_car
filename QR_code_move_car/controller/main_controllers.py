from flask import Flask
from flask_restful import Api

from QR_code_move_car.views.Login_Views import Login
from QR_code_move_car.views.QRCode_Views import Apply_QrCode
from QR_code_move_car.views.Register_Views import Register
from QR_code_move_car.views.Verify_Views import Verify

app = Flask(__name__)
api = Api(app)

api.add_resource(Login, '/login/<id>')
api.add_resource(Verify, '/verify/')
api.add_resource(Register, '/register/')
api.add_resource(Apply_QrCode, '/qrcode/')