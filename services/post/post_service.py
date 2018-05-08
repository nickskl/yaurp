from services.post import app
from flask_restful import Api
from services.post.rest_api.post_resource import *
from services.post .config import current_config
from services.post.security.security import context


app.config.from_object(current_config)
api = Api(app)
service_namespace = "/posts"

api.add_resource(PostResource,  current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH +
                 current_config.POST_URL_PATH)
api.add_resource(PostListResource,  current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH)
api.add_resource(PostCreateResource,  current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH +
                 current_config.POST_CREATE_URL_PATH)


if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run()