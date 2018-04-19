import itsdangerous
import crypt
import datetime
from services.user.config import *
import jsonpickle
from services.user.helper import *
import dateutil.parser


config = DevelopmentConfig


class Token:
    def __init__(self, value, expiration):
        self.value = value
        self.expiration = expiration.isoformat()

    @staticmethod
    def generate(value):
        serializer = itsdangerous.Serializer(Config.SECRET_KEY, crypt.mksalt(crypt.METHOD_SHA512))
        return Token(serializer.dumps(value), datetime.datetime.now() +
                     datetime.timedelta(0, config.TOKEN_EXPIRATION_TIME))

    def serialize(self):
        serializer = itsdangerous.Serializer(Config.SECRET_KEY)
        return serializer.dumps(self.__dict__)

    @staticmethod
    def is_expired(token_string):
        if token_string is None:
            return True
        serializer = itsdangerous.Serializer(Config.SECRET_KEY)
        token = serializer.loads(token_string)
        return dateutil.parser.parse(token.expiration) >= datetime.datetime.now()

    @staticmethod
    def refresh(token_string):
        serializer = itsdangerous.Serializer(Config.SECRET_KEY)
        token = serializer.loads(token_string)
        token.expiration = (datetime.datetime.now() + datetime.timedelta(0, config.TOKEN_EXPIRATION_TIME)).isoformat()
        return serializer.dumps(token)
