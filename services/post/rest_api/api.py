from flask_restful import Api
import flask
from services.post.rest_api.post_resource import PostListResource, PostResource

app = flask.current_app
api = Api(app)
service_namespace = "/posts"

api.add_resource(PostResource, service_namespace.join("/<post_id>"))
api.add_resource(PostListResource, service_namespace)
