from flask_restful import Api

from Settings.configuration import create_app
from views.Login_Views import Login
from views.QRCode_Views import Apply_QrCode
from views.Register_Views import Register
from views.Verify_Views import Verify

app = create_app("dev")
api = Api(app)

api.add_resource(Login, '/login/<id>')
api.add_resource(Verify, '/verify/<uuid>')
api.add_resource(Register, '/register/')
api.add_resource(Apply_QrCode, '/qrcode/')