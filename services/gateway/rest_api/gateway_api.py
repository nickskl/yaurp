from flask_restful import Resource, reqparse
import flask
from services.gateway.config import Config
import requests

parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)
parser.add_argument("role", type=str)


class GatewayPostResource(Resource):
    def get(self, post_id):
        return requests.get(Config.POST_SERVICE_URL + "/%d" % post_id)
    def post(self, post_id, ):
        pass


class GatewayPostListResource(Resource):
    def get(self):
        return None


class GatewayAuthorizationResource(Resource):
    def get(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        args = parser.parse_args(strict=True)
        role = args['role']
        payload = (('role', role), )
        resp = sess.get("http://127.0.0.1:1234" + Config.USER_SERVICE_URL + Config.AUTH_URL_PATH, params=payload)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items())
        return result


class GatewayTokenResource(Resource):
    def get(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        args = parser.parse_args(strict=True)
        login = args['login']
        password = args['password']
        payload = (('login', login), ('password', password))
        resp = sess.get("http://127.0.0.1:1234" + Config.USER_SERVICE_URL + Config.TOKEN_URL_PATH, params=payload)

        result = flask.Response(status=resp.status_code,headers=resp.headers.items())
        result.set_cookie('token', sess.cookies['token'])
        return result