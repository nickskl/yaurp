

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""
    SECRET_KEY = "qwerty1234"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GATEWAY_URL = "/gateway"
    POST_SERVICE_URL = "/posts"
    USER_SERVICE_URL = "/users"
    AUTH_URL_PATH = "/auth"
    TOKEN_URL_PATH = "/token"
    STATISTICS_SERVICE_URL = "/statistics"


class DevelopmentConfig(Config):
    DEBUG = True