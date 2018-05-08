

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SECRET_KEY = "qwerty1234"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STAT_SERVICE_PATH = "/statistics"

    GATEWAY_URL_PATH = "/gateway/api"
    CHECK_ROLE_URL_PATH = "/auth/check_role"
    GET_TOKEN_URL_PATH = "/auth/token"
    TOKEN_CHECK_ID_URL_PATH = "/auth/token/check_id"


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5001
    USER_SERVICE_URL = "http://127.0.0.1:%d" % PORT
    GATEWAY_SERVICE_URL = "http://127.0.0.1:5000"

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://tester:111@localhost/users_db"
    TOKEN_EXPIRATION_TIME = 2000
    TRUSTED_SERVICE = "gateway"

current_config = DevelopmentConfig()