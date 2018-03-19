from flask_restful import  Resource


def abort_if_post_doesnt_exist(post_id):
    pass


class PostResource(Resource):
    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
