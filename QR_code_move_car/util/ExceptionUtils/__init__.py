class InvalidOperation(Exception):
    def __init__(self, message):
        self.message = message or "InvalidOperation"


class DBException(InvalidOperation, Exception):
    pass


class RedisException(InvalidOperation, Exception):
    pass

