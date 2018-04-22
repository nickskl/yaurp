from flask_restful import Resource, abort, reqparse
from flask import request, jsonify
from services.user import app
from services.user.domain.user import User
from services.user.repository.user_repository import UserRepository
import jsonpickle


repo = UserRepository()
parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)
parser.add_argument("role", type=str)


class UserResource(Resource):
    def get(self):
        if 'token' in request.cookies:
            args = parser.parse_args(strict=True)
            if "login" not in args:
                response = app.make_response("User credentials not supplied")
                response.status_code = 400
                return response
            token = request.cookies['token']
            user = repo.get_by_token(token)
            if user is not None:
                result = repo.refresh_token(token)
                if result is not None:
                    result = repo.get_user(args['login'])
                    if result is not None:
                        return jsonpickle.encode(User(identifier=result.id, username=result.login,
                            active=result.active))
                else:
                    response = app.make_response("Token expired")
                    response.status_code = 403
                    return response
            else:
                response = app.make_response("The token in request not associated with any user")
                response.status_code = 403
                return response
        response = app.make_response("No valid token supplied")
        response.status_code = 403
        return response

    def delete(self, user_id):
        pass

    def post(self):
        pass


class UserAuthorizationResource(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        if "login" not in args or "password" not in args:
            response = app.make_response("User credentials not supplied")
            response.status_code = 400
            return response
        token = repo.get_token(args["login"], args["password"])
        if token is not None:
            user = repo.get_by_token(token)
            if user is not None:
                response = app.make_response("Token generated")
                response.status_code = 200
                response.set_cookie('token', value=token)
                return response
        response = app.make_response("Incorrect user credentials")
        response.status_code = 403
        return response

    def put(self):
        if 'token' in request.cookies:
            token = request.cookies['token']
            user = repo.get_by_token(token)
            result = repo.refresh_token(user.login)
            if result is not None:
                response = app.make_response("Token refreshed")
                response.status_code = 200
                response.set_cookie('token', value=token)
            else:
                response = app.make_response("The token in request not associated with any user")
                response.status_code = 403
                response.delete_cookie('token')
            return response
        response = app.make_response("No valid token supplied")
        response.status_code = 403
        return response


class UserRoleResource(Resource):
    def get(self):
        if 'token' in request.cookies:
            args = parser.parse_args(strict=True)
            if "role" not in args:
                response = app.make_response("Role parameter is not set")
                response.status_code = 400
                return response
            token = request.cookies['token']
            user = repo.get_by_token(token)
            if user is not None:
                result = repo.refresh_token(token)
                if result is not None:
                    response = app.make_response("")
                    response.status_code = 200
                    is_role = False
                    for role in user.roles:
                        is_role = is_role or (role.name == args['role'])
                    response.data = jsonpickle.encode(is_role)
                    response.set_cookie('token', value=result)
                else:
                    response = app.make_response("Token expired")
                    response.status_code = 403
                    return response
            else:
                response = app.make_response("The token in request not associated with any user")
                response.status_code = 403
                return response
        response = app.make_response("No valid token supplied")
        response.status_code = 403
        return response


class UserIdCheckResource(Resource):
    def get(self):
        if 'token' in request.cookies:
            args = parser.parse_args(strict=True)
            if "id" not in args:
                response = app.make_response("Id parameter is not set")
                response.status_code = 400
                return response
            id = args["id"]
            token = request.cookies['token']
            user = repo.get_by_token(token)
            if user is not None:
                result = repo.refresh_token(token)
                if result is not None:
                    response = app.make_response("")
                    response.status_code = 200
                    is_id = id == user.id
                    response.data = jsonpickle.encode(is_id)
                    response.set_cookie('token', value=result)
                else:
                    response = app.make_response("Token expired")
                    response.status_code = 403
                    return response
            else:
                response = app.make_response("The token in request not associated with any user")
                response.status_code = 403
                return response
        response = app.make_response("No valid token supplied")
        response.status_code = 403
        return response
