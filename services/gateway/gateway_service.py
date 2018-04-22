from services.post import app
from flask_restful import Api
from services.post.rest_api.post_resource import PostListResource, PostResource
from services.post.config import DevelopmentConfig
from services.post.security.security import context
from services.gateway.rest_api.gateway_api import *


app.config.from_object(DevelopmentConfig)
api = Api(app)
service_namespace = "/gateway"

#api.add_resource(PostResource, service_namespace + "/<post_id>")
#api.add_resource(PostListResource, service_namespace)
api.add_resource(GatewayAuthorizationResource, Config.GATEWAY_URL + Config.USER_SERVICE_PATH + Config.CHECK_ROLE_URL_PATH)
api.add_resource(GatewayTokenResource, Config.GATEWAY_URL + Config.USER_SERVICE_PATH + Config.GET_TOKEN_URL_PATH)
api.add_resource(GatewayTokenGetUserIdResource, Config.GATEWAY_URL + Config.USER_SERVICE_PATH + Config.TOKEN_CHECK_ID_URL_PATH)

if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run()