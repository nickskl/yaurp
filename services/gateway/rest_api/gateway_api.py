from flask_restful import Resource, reqparse
import flask
from services.gateway.config import current_config
import requests
import jsonpickle


class GatewayPostResource(Resource):
    def get(self, post_id):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = requests.get(current_config.POST_SERVICE_PATH + "/%d" % post_id)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def post(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.post(current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH, data=flask.request.data)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def patch(self, post_id):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.patch(current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH + "/%d" % post_id,
                          data=flask.request.data)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def delete(self, post_id):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.delete(current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH + "/%d" % post_id)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result


class GatewayPostListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("criteria", type=str)
    parser.add_argument("search_value", type=str)

    def get(self):
        sess = requests.session()
        args = self.parser.parse_args()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        payload = (('criteria', args['criteria']), ('search_value', args['search_value']))
        resp = requests.get(current_config.POST_SERVICE_URL + current_config.POST_SERVICE_PATH, params=payload)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result


class GatewayUserInfoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("password", type=str)

    def get(self, user_id):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.get(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH +
                        current_config.USER_URL_PATH + "/%d" % user_id)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def patch(self, user_id):
        sess = requests.session()
        args = self.parser.parse_args()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.patch(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.USER_URL_PATH +
                          "/%d" % user_id, jsonpickle.encode({"password": args["password"]}))
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def delete(self, user_id):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.delete(
            current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.USER_URL_PATH + "/%d" % user_id)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result


class GatewayUserRoleResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("role", type=str)

    def get(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        args = self.parser.parse_args(strict=True)
        role = args['role']
        payload = (('role', role), )
        resp = sess.get(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.CHECK_ROLE_URL_PATH,
                        params=payload)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result


class GatewayUserAuthorizationResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("login", type=str)
    parser.add_argument("password", type=str)
    parser.add_argument("role", type='str')


    def get(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        args = self.parser.parse_args(strict=True)
        login = args['login']
        password = args['password']
        payload = (('login', login), ('password', password))
        resp = sess.get(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.GET_TOKEN_URL_PATH,
                        params=payload)
        result = flask.Response(status=resp.status_code,headers=resp.headers.items(), response=resp.content)
        return result

    def post(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        args = self.parser.parse_args(strict=True)
        login = args['login']
        password = args['password']
        if 'role' in args and args['role'] is not None:
            payload = (('login', login), ('password', password), ('role', args['role']))
        else:
            payload = (('login', login), ('password', password))
        resp = sess.post(
            current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.GET_TOKEN_URL_PATH,
            params=payload)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def put(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.put(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.GET_TOKEN_URL_PATH,
                        data=jsonpickle.encode({}))
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result


class GatewayUserIdCheckResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int)

    def get(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        args = self.parser.parse_args(strict=True)
        id = args['id']
        payload = (('id', id),)
        resp = sess.get(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH + current_config.TOKEN_CHECK_ID_URL_PATH,
                        params=payload)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result


class GatewayStatisticsResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("service_token", type=str)

    def get(self):
        sess = requests.session()
        for cookie in flask.request.cookies:
            sess.cookies[cookie] = flask.request.cookies[cookie]
        resp = sess.get(current_config.STATISTICS_SERVICE_URL + current_config.STATISTICS_SERVICE_PATH)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result

    def post(self):
        sess = requests.session()
        args = self.parser.parse_args(strict=True)
        service_token = args['service_token']
        payload = (('service_token', service_token),)
        resp = sess.post(current_config.USER_SERVICE_URL + current_config.USER_SERVICE_PATH +
                         current_config.TOKEN_CHECK_ID_URL_PATH, params=payload, data=flask.request.data)
        result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
        return result
