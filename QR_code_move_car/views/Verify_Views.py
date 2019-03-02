from flask import make_response
from flask_restful import Resource

from QR_code_move_car.constants import REDIS_EXPIRE_TIME
from QR_code_move_car.lib.captcha.captcha import captcha
from QR_code_move_car.util.DbOperation.redis_utils import OperationRedis


class Verify(Resource):
    def get(self, uuid):
        redis_instance = OperationRedis.get_redis()
        _, code, image = captcha.gererate_pic()
        redis_instance.set(uuid, code, REDIS_EXPIRE_TIME)
        response = make_response(image)
        response.content_type = "img/png·"
        return response


    def post(self):
        # TODO: need arguments uuid, code, mobile
        pass