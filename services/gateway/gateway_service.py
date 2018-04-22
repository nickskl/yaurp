from services.post import app
from flask_restful import Api
from services.post.rest_api.post_resource import PostListResource, PostResource
from services.post.config import DevelopmentConfig
from services.post.security.security import context
from services.gateway.rest_api.gateway_api import *


app.config.from_object(DevelopmentConfig)
api = Api(app)

api.add_resource(PostResource, Config.GATEWAY_PATH + Config.POST_SERVICE_PATH + "/<post_id>")
api.add_resource(PostListResource, Config.GATEWAY_PATH + Config.POST_SERVICE_PATH)
api.add_resource(GatewayUserRoleResource, Config.GATEWAY_PATH + Config.USER_SERVICE_PATH + Config.CHECK_ROLE_URL_PATH)
api.add_resource(GatewayUserAuthorizationResource, Config.GATEWAY_PATH + Config.USER_SERVICE_PATH +
                 Config.GET_TOKEN_URL_PATH)
api.add_resource(GatewayUserIdCheckResource, Config.GATEWAY_PATH + Config.USER_SERVICE_PATH +
                 Config.TOKEN_CHECK_ID_URL_PATH)
api.add_resource(GatewayUserInfoResource, Config.GATEWAY_PATH + Config.USER_SERVICE_PATH + Config.USER_URL_PATH)
api.add_resource(GatewayStatisticsResource, Config.GATEWAY_PATH + Config.STATISTICS_SERVICE_PATH)

if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run()
