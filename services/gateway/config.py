

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "qwerty1234"
    GATEWAY_PATH = "/gateway/api"

    POST_SERVICE_PATH = "/posts"

    STATISTICS_SERVICE_PATH = "/statistics"

    USER_SERVICE_PATH = "/users"

    USER_URL_PATH = "/<user_id>"
    CHECK_ROLE_URL_PATH = "/auth/check_role"
    GET_TOKEN_URL_PATH = "/auth/token"
    TOKEN_CHECK_ID_URL_PATH = "/auth/token/check_id"


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5000
    USER_SERVICE_URL = "http://127.0.0.1:5001"
    POST_SERVICE_URL = "http://127.0.0.1:5002"
    STATISTICS_SERVICE_URL = "http://127.0.0.1:5003"
