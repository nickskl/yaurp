from flask_restful import Resource, abort, reqparse
from flask_login import login_required
from services.post.repository.post_repository import PostRepository
from services.post.security.security import check_current_user_id, check_if_current_user_is_privileged
from services.post import app
from datetime import *


repo = PostRepository(app)
parser = reqparse.RequestParser()
parser.add_argument("user_id", type=int)
parser.add_argument("date", type=lambda x: datetime.strptime(x,"%d-%m-%Y %H:%M:%S"))
parser.add_argument("text")
parser.add_argument("criteria", type=dict)


def abort_if_post_doesnt_exist(post_id):
    if not repo.exists(post_id):
        abort(404, message="Post {} doesn't exist".format(post_id))


class PostResource(Resource):
    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        return repo.get(post_id)

    def delete(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        post = repo.get(post_id)
        if (check_current_user_id(post.user_id) or
            check_if_current_user_is_privileged()):

            repo.delete(post_id)
            return '', 204
        else:
            abort(403, message="You have not enough privileges to delete selected post")

    def patch(self, post_id):
        args = parser.parse_args(strict=True)
        abort_if_post_doesnt_exist(post_id)
        post_id = repo.update(post_id, args["user_id"], args["date"], args["text"])
        return repo.get(post_id), 201


class PostListResource(Resource):
    def get(self, criteria = None):
        return repo.read_all_by_criteria(criteria)

    def post(self):
        args = parser.parse_args(strict=True)
        post_id = repo.create(args["user_id"], args["date"], args["text"])
        return repo.get(post_id), 201
