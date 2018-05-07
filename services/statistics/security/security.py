from OpenSSL import SSL
from services.statistics.config import *
import flask
import requests
import jsonpickle

context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_privatekey("./user.key")
#context.use_certificate("./user.crt")


def check_value(value):
    sess = requests.session()
    for cookie in flask.request.cookies:
        sess.cookies[cookie] = flask.request.cookies[cookie]
    payload = (("id", value),)
    resp = sess.get(DevelopmentConfig.GATEWAY_SERVICE_URL + Config.GATEWAY_URL_PATH +
                    Config.TOKEN_CHECK_ID_URL_PATH, params=payload)
    result = flask.Response(status=resp.status_code, headers=resp.headers.items(), response=resp.content)
    return result


def check_if_current_user_is_privileged():
    sess = requests.session()
    for cookie in flask.request.cookies:
        sess.cookies[cookie] = flask.request.cookies[cookie]
    payload = (("role", "admin"),)
    resp = sess.get(DevelopmentConfig.GATEWAY_SERVICE_URL + Config.GATEWAY_URL_PATH +
                    Config.CHECK_ROLE_URL_PATH, params=payload)
    result = jsonpickle.decode(resp.content)
    return result
