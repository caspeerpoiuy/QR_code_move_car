from flask import make_response, request
from flask_restful import Resource

from constants import REDIS_EXPIRE_TIME
from lib.captcha.captcha import captcha
from util.DbOperation.redis_utils import OperationRedis
from util.ExceptionUtils import RedisException


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


def post():
    mobile = request.json.get("mobile")
    image_code = request.json.get("image_code")
    uuid = request.json.get("uuid")
    if not all([mobile, image_code, uuid]):
        return
    try:
        redis_image = OperationRedis.get_redis().get(uuid)
    except Exception as e:
        print(e)
    if not redis_image:
        return
