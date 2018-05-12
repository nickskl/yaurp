from functools import wraps
from flask import g, url_for, flash, abort, request, redirect, make_response
import requests
import requests.exceptions
from services.gui.config import current_config
import jsonpickle


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash('Войдите для просмотра данной страницы')
            return redirect(url_for('user.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.is_admin:
            abort(401)
        return f(*args, **kwargs)
    return requires_login(decorated_function)


def requires_publisher(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.user.is_publisher and not g.user.is_admin:
            abort(401)
        return f(*args, **kwargs)
    return requires_login(decorated_function)


def request_handler(redirect_url):
    def wrap(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                request_result = f(*args, **kwargs)
                return Result(success=True, redirect=redirect_url, response=request_result)
            except requests.exceptions.Timeout as e:
                return Result(success=False, error='Время ожидания ответа превышено. Повторите запрос позже')
            except requests.exceptions.ConnectionError as e:
                return Result(success=False, error='В данный момент сервис недоступен. Повторите запрос позже')
            except requests.exceptions.RequestException as e:
                return Result(success=False, error='Произошла ошибка. Повторите запрос позже')
        return decorated_function
    return wrap


class Result:
    def __init__(self, success, response=None, error=None, redirect=None):
        self.success = success
        self.error = error
        self.redirect = redirect
        self.response = response


@request_handler(redirect_url='posts.index')
def do_login(login, password):
    result = gateway_api_request(current_config.USER_SERVICE_PATH, current_config.GET_TOKEN_URL_PATH, 'GET',
                                 (('login', login),('password', password)))
    return result


@request_handler(redirect_url='posts.index')
def do_logout():
    response = make_response("")
    if 'token' in request.cookies:
        response.delete_cookie('token')
    return response


@request_handler(redirect_url='posts.index')
def do_register(login, password, role):
    if role is not None:
        result = gateway_api_request(current_config.USER_SERVICE_PATH, current_config.GET_TOKEN_URL_PATH, 'POST',
                                 (('login', login),('password', password), ('role', role)))
    else:
        result = gateway_api_request(current_config.USER_SERVICE_PATH, current_config.GET_TOKEN_URL_PATH, 'POST',
                                     (('login', login), ('password', password)))

    return result

@request_handler(None)
def do_check_admin(cookies):
    result = gateway_api_request(current_config.USER_SERVICE_PATH, current_config.CHECK_ROLE_URL_PATH, 'GET',
                                 (('role', 'admin'), ), cookies=cookies)
    return result


@request_handler(None)
def do_check_publisher(cookies):
    result = gateway_api_request(current_config.USER_SERVICE_PATH, current_config.CHECK_ROLE_URL_PATH, 'GET',
                                 (('role', 'publisher'),), cookies=cookies)
    return result


@request_handler(redirect_url='statistics.index')
def do_get_statistics(cookies):
    result = gateway_api_request(current_config.STATISTICS_SERVICE_PATH, current_config.GET_STATISTICS_PATH, 'GET',
                                 cookies=cookies)
    return result

def gateway_api_request(service_path, request_path, method, params=None, data=None, cookies=None):
    if method == 'GET':
        return requests.get(current_config.GATEWAY_SERVICE_URL + current_config.GATEWAY_SERVICE_PATH
                         + service_path + request_path, params=params, cookies=cookies)
    elif method == 'POST':
        return requests.post(current_config.GATEWAY_SERVICE_URL + current_config.GATEWAY_SERVICE_PATH
                         + service_path + request_path, data, params=params, cookies=cookies)
    elif method == 'PUT':
        return requests.put(current_config.GATEWAY_SERVICE_URL + current_config.GATEWAY_SERVICE_PATH
                         + service_path + request_path, data, params=params, cookies=cookies)
    elif method == 'DELETE':
        return requests.delete(current_config.GATEWAY_SERVICE_URL + current_config.GATEWAY_SERVICE_PATH
                         + service_path + request_path, cookies=cookies)
    elif method == 'PATCH':
        return requests.patch(current_config.GATEWAY_SERVICE_URL + current_config.GATEWAY_SERVICE_PATH
                         + service_path + request_path, data, cookies=cookies)
    else:
        abort(400)
