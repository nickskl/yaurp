from services.user import app
from flask_restful import Api
from services.user.rest_api.user_resource import *
from services.user.config import Config

api = Api(app)

api.add_resource(UserResource, Config.USER_SERVICE_PATH + Config.USER_URL_PATH)
api.add_resource(UserAuthorizationResource, Config.USER_SERVICE_PATH + Config.GET_TOKEN_URL_PATH)
api.add_resource(UserRoleResource, Config.USER_SERVICE_PATH + Config.CHECK_ROLE_URL_PATH)
api.add_resource(UserIdCheckResource, Config.USER_SERVICE_PATH + Config.TOKEN_CHECK_ID_URL_PATH)


if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run()