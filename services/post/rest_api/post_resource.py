from flask_restful import Resource, abort, reqparse
import flask
from services.post.repository.post_repository import PostRepository
from services.post.security.security import check_current_user_id, check_if_current_user_is_privileged
from services.post import app
import jsonpickle


repo = PostRepository()


def abort_if_post_doesnt_exist(post_id):
    if not repo.exists(post_id):
        abort(404, message="Post {} doesn't exist".format(post_id))


class PostResource(Resource):

    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        post = repo.get(post_id)
        response = app.make_response("")
        response.status_code = 200
        response.data = jsonpickle.encode(post)
        return response

    def delete(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        post = repo.get(post_id)
        if (check_current_user_id(post.user_id) or
           check_if_current_user_is_privileged()):

            repo.delete(post_id)
            response = app.make_response("Post %d deleted successfully" % post_id)
            response.status_code = 204
            return response
        abort(403, message="You have not enough privileges to delete selected post")

    def patch(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        payload = jsonpickle.decode(flask.request.data)
        user_id = repo.get(post_id).user_id
        if ((check_current_user_id(payload["user_id"]) and
             check_current_user_id(user_id)) or check_if_current_user_is_privileged()):
            repo.update(post_id, payload["user_id"], payload["title"], payload["text"])
            post = repo.get(post_id)
            response = app.make_response("")
            response.status_code = 201
            response.data = jsonpickle.encode(post)
            return response
        abort(403, message="You have not enough privileges to delete selected post")


class PostCreateResource(Resource):

    def post(self):
        abort_if_post_doesnt_exist(post_id)
        payload = jsonpickle.decode(flask.request.data)
        if (not check_if_user_is_guest() and
                check_current_user_id(payload["user_id"])):

            post_id = repo.create(args["user_id"], args["date"], args["text"])
        return repo.get(post_id), 201


class PostListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("criteria", type=str)
    parser.add_argument("search_value", type=str)

    def get(self, criteria = None):
        return repo.read_all_by_criteria(criteria)
