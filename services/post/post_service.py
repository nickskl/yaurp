from services.post import app
from flask_restful import Api
from services.post.rest_api.post_resource import PostListResource, PostResource

api = Api(app)
service_namespace = "/posts"

api.add_resource(PostResource, service_namespace + "/<post_id>")
api.add_resource(PostListResource, service_namespace)


if __name__ == '__main__':
    app.run(debug=True)