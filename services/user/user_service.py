from services.user import app
from flask_restful import Api
from services.user.rest_api.user_resource import *
from services.user.config import current_config

api = Api(app)

api.add_resource(UserResource, current_config.USER_SERVICE_PATH + current_config.USER_URL_PATH)
api.add_resource(UserAuthorizationResource, current_config.USER_SERVICE_PATH + current_config.GET_TOKEN_URL_PATH)
api.add_resource(UserRoleResource, current_config.USER_SERVICE_PATH + current_config.CHECK_ROLE_URL_PATH)
api.add_resource(UserIdCheckResource, current_config.USER_SERVICE_PATH + current_config.TOKEN_CHECK_ID_URL_PATH)


if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run(port=current_config.PORT)