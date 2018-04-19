from services.post import app
from flask_restful import Api
from services.post.rest_api.post_resource import PostListResource, PostResource
from services.post.config import DevelopmentConfig
from services.post.security.security import context


app.config.from_object(DevelopmentConfig)
api = Api(app)
service_namespace = "/posts"

api.add_resource(PostResource, service_namespace + "/<post_id>")
api.add_resource(PostListResource, service_namespace)


if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run(debug=True, port=5001)