from services.post import app
from flask_restful import Api
from services.post.rest_api.post_resource import PostListResource, PostResource
from services.post.config import current_config
from services.post.security.security import context
from services.gateway.rest_api.gateway_api import *


app.config.from_object( current_config)
api = Api(app)

api.add_resource(PostResource, current_config.GATEWAY_PATH + current_config.POST_SERVICE_PATH + "/<post_id>")
api.add_resource(PostListResource, current_config.GATEWAY_PATH + current_config.POST_SERVICE_PATH)
api.add_resource(GatewayUserRoleResource, current_config.GATEWAY_PATH + current_config.USER_SERVICE_PATH + current_config.CHECK_ROLE_URL_PATH)
api.add_resource(GatewayUserAuthorizationResource, current_config.GATEWAY_PATH + current_config.USER_SERVICE_PATH +
                 current_config.GET_TOKEN_URL_PATH)
api.add_resource(GatewayUserIdCheckResource, current_config.GATEWAY_PATH + current_config.USER_SERVICE_PATH +
                 current_config.TOKEN_CHECK_ID_URL_PATH)
api.add_resource(GatewayUserInfoResource, current_config.GATEWAY_PATH + current_config.USER_SERVICE_PATH + current_config.USER_URL_PATH)
api.add_resource(GatewayStatisticsResource, current_config.GATEWAY_PATH + current_config.STATISTICS_SERVICE_PATH)

if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run()
