import itsdangerous
import datetime
from services.user .config import current_config
import dateutil.parser


config = DevelopmentConfig


class Token:
    def __init__(self, value, expiration):
        self.value = value
        self.expiration = expiration.isoformat()

    @staticmethod
    def generate(value):
        serializer = itsdangerous.Serializer(current_config.SECRET_KEY)
        return Token(serializer.dumps(value), datetime.datetime.now() +
                     datetime.timedelta(0, config.TOKEN_EXPIRATION_TIME))

    def serialize(self):
        serializer = itsdangerous.Serializer(current_config.SECRET_KEY)
        return serializer.dumps(self.__dict__)

    @staticmethod
    def is_expired(token_string):
        if token_string is None:
            return True
        serializer = itsdangerous.Serializer(current_config.SECRET_KEY)
        token = serializer.loads(token_string)
        return dateutil.parser.parse(token['expiration']) < datetime.datetime.now()

    @staticmethod
    def check_value(token_string, value):
        if token_string is None:
            return False
        serializer = itsdangerous.Serializer(current_config.SECRET_KEY)
        token = serializer.loads(token_string)
        return serializer.loads(token['value']) == value

    @staticmethod
    def get_value(token_string):
        if token_string is None:
            return False
        serializer = itsdangerous.Serializer(current_config.SECRET_KEY)
        token = serializer.loads(token_string)
        return serializer.loads(token['value'])

    @staticmethod
    def refresh(token_string):
        serializer = itsdangerous.Serializer(current_config.SECRET_KEY)
        token = serializer.loads(token_string)
        token['expiration'] = (datetime.datetime.now() + datetime.timedelta(seconds=config.TOKEN_EXPIRATION_TIME)).isoformat()
        return serializer.dumps(token)
