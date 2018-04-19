from services.user import app
from flask_restful import Api
from services.user.rest_api.user_resource import *


api = Api(app)
service_namespace = "/users"

api.add_resource(UserResource, service_namespace + "/<user_id>")
api.add_resource(UserTokenResource, service_namespace + "/token")
api.add_resource(AuthorizationResource, service_namespace + "/auth")

if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run(debug=True, port=1234)