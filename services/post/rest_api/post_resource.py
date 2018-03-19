from flask_restful import  Resource, abort, reqparse
from services.post.repository.post_repository import PostRepository
from services.post import app
from datetime import *

repo = PostRepository(app)
parser = reqparse.RequestParser()
parser.add_argument("user_id", type=int)
parser.add_argument("date", type=lambda x: datetime.strptime(x,"%d-%m-%Y %H:%M:%S"))
parser.add_argument("text")


def abort_if_post_doesnt_exist(post_id):
    if not repo.exists(post_id):
        abort(404, message="Post {} doesn't exist".format(post_id))


class PostResource(Resource):
    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        return repo.read(post_id)

    def delete(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        repo.delete(post_id)
        return '', 204

    def patch(self, post_id):
        args = parser.parse_args(strict=True)
        abort_if_post_doesnt_exist(post_id)
        post_id = repo.update(post_id, args["user_id"], args["date"], args["text"])
        return repo.read(post_id), 201


class PostListResource(Resource):
    def get(self):
        return repo.read_all()

    def post(self):
        args = parser.parse_args(strict=True)
        post_id = repo.create(args["user_id"], args["date"], args["text"])
        return repo.read(post_id), 201
