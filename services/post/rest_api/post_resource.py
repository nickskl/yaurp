from flask_restful import  Resource
from services.post.repository.post_repository import PostRepository
import flask


repo = PostRepository(flask.current_app)

def abort_if_post_doesnt_exist(post_id):
    repo.


class PostResource(Resource):
    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
