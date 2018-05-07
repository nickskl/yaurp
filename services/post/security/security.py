from OpenSSL import SSL
from services.post.config import *
import flask
from flask_restful import reqparse
import requests
import jsonpickle


parser = reqparse.RequestParser()
# parser.add_argument("login", type=str)


context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./post.key")
#context.use_certificate("./post.crt")


def check_current_user_id(expected_id):
    sess = requests.session()
    for cookie in flask.request.cookies:
        sess.cookies[cookie] = flask.request.cookies[cookie]
    payload = (("id", expected_id),)
    resp = sess.get(DevelopmentConfig.GATEWAY_SERVICE_URL + Config.GATEWAY_SERVICE_PATH +
                    Config.TOKEN_CHECK_ID_URL_PATH, params=payload)
    result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
    return result


def check_if_current_user_is_guest():
    sess = requests.session()
    for cookie in flask.request.cookies:
        sess.cookies[cookie] = flask.request.cookies[cookie]
    payload = (("role", "user"),)
    resp = sess.get(DevelopmentConfig.GATEWAY_SERVICE_URL + Config.GATEWAY_SERVICE_PATH + Config.CHECK_ROLE_URL_PATH,
                    params=payload)
    return resp.status_code != 200


def check_if_current_user_is_privileged():
    sess = requests.session()
    for cookie in flask.request.cookies:
        sess.cookies[cookie] = flask.request.cookies[cookie]
    payload = (("role", "admin"),)
    resp = sess.get(DevelopmentConfig.GATEWAY_SERVICE_URL + Config.GATEWAY_SERVICE_PATH +
                    Config.CHECK_ROLE_URL_PATH, params=payload)
    result = jsonpickle.decode(resp.content)
    return result
