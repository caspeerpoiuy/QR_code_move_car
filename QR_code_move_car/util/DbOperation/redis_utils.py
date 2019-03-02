import redis


class OperationRedis(object):
    @staticmethod
    def get_redis(host="127.0.0.1", port=6379, hub_num=0):
        return redis.Redis(host=host, port=port, db=hub_num)
