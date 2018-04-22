

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SECRET_KEY = "qwerty1234"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GATEWAY_URL = "/gateway"
    AUTH_URL_PATH = "/auth"
    TOKEN_URL_PATH = "/token"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://tester:111@localhost/posts_db"