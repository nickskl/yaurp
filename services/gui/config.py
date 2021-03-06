

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SECRET_KEY = "qwerty1234"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POST_SERVICE_PATH = "/posts"

    STATISTICS_SERVICE_PATH = "/statistics"

    USER_SERVICE_PATH = "/users"

    POST_URL_PATH = "/<post_id>"
    POST_CREATE_URL_PATH = "/create"

    GATEWAY_SERVICE_PATH = "/gateway/api"

    CHECK_ROLE_URL_PATH = "/auth/check_role"
    GET_TOKEN_URL_PATH = "/auth/token"
    TOKEN_CHECK_ID_URL_PATH = "/auth/token/check_id"

    GET_STATISTICS_PATH = "/get"

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5005
    GUI_SERVICE_URL = "http://127.0.0.1:%d" % PORT
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://tester:111@localhost/posts_db"
    GATEWAY_SERVICE_URL = "http://127.0.0.1:5000"


current_config = DevelopmentConfig()