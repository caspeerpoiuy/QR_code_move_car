from flask_restful import Resource


class Login(Resource):
    @staticmethod
    def get(id):
        # TODO: need to return a login template
        return {'hello': id}

    def post(self):
        # request.
        pass