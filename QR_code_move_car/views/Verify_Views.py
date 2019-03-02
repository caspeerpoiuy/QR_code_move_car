from flask_restful import Resource


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