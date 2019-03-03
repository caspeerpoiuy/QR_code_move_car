from flask import make_response
from flask_restful import Resource

from QR_code_move_car.constants import REDIS_EXPIRE_TIME
from QR_code_move_car.lib.captcha.captcha import captcha
from QR_code_move_car.util.DbOperation.redis_utils import OperationRedis
from QR_code_move_car.util.ExceptionUtils import RedisException


class Verify(Resource):
    @staticmethod
    def get(uuid):
        if not uuid:
            return
        redis_instance = OperationRedis.get_redis()
        _, code, image = captcha.gererate_pic()
        try:
            redis_instance.set(uuid, code, REDIS_EXPIRE_TIME)
        except RedisException as e:
            print(e)
        response = make_response(image)
        response.content_type = "img/png·"
        return response

    @staticmethod
    def post():
        # TODO: need arguments uuid, code, mobile
        pass