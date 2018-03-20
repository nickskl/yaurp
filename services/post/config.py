

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ""
    SECRET_KEY = "qwerty1234"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = "postgresql://admin:QAZxsw2!@localhost/posts_db"