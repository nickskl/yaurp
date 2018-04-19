from flask_restful import Resource, abort, reqparse
from services.user.security.security import refresh_token, get_user_by_token, get_token, check_role
from flask import request, jsonify
from services.user import app
from services.user.domain.user import User
from services.user.security.security import user_datastore
import jsonpickle


parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)
parser.add_argument("role", type=str)


class UserResource(Resource):
    def get(self, user_id):
        result = user_datastore.find_user(id=user_id)
        if result is not None:
            return jsonpickle.encode(User(identifier=user_id,
                        username=result.login,
                        password=result.password,
                        active=result.active,
                        token=result.token))
        return None

    def delete(self, user_id):
        pass

    def post(self):
        pass


class UserTokenResource(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        token = get_token(args["login"], args["password"])
        user = get_user_by_token(token)
        if token is not None:
            response = app.make_response("")
            response.status_code = 200
            response.set_cookie('token', value=token)
            return response
        response = app.make_response("")
        response.status_code = 403
        return response

    def put(self):
        if 'token' in request.cookies:
            token = request.cookies['token']
            result = refresh_token(token)
            if result is not None:
                response = app.make_response("")
                response.status_code = 200
                response.set_cookie('token', value=token)
            else:
                response = app.make_response("")
                response.status_code = 403
                response.delete_cookie('token')
            return response
        response = app.make_response("")
        response.status_code = 403
        return response


class AuthorizationResource(Resource):
    def get(self):
        if 'token' in request.cookies:
            args = parser.parse_args(strict=True)
            token = request.cookies['token']
            result = refresh_token(token)
            if result is not None:
                user = get_user_by_token(token)
                response = app.make_response("")
                response.status_code = 200
                response.data = jsonify(check_role(user.id, args["role"]))
                response.set_cookie('token', value=token)
            else:
                response = app.make_response("")
                response.status_code = 403
                response.delete_cookie('token')
            return response
        response = app.make_response("")
        response.status_code = 403
        return response