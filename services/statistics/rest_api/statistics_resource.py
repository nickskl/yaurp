from flask_restful import Resource, abort, reqparse
from flask import request, jsonify
from services.statistics import app
from services.statistics.repository.statistics_repository import StatisticsRepository
import jsonpickle
from services.statistics.security.security import *

repo = StatisticsRepository()
parser = reqparse.RequestParser()
parser.add_argument("type", type=str)


class StatisticsResource(Resource):
    def get(self):
        if 'token' in request.cookies:
            result = check_if_current_user_is_privileged()
            if result:
                args = parser.parse_args(strict=True)
                if 'type' not in args:
                    response = app.make_response("Тип возвращаемой статистики не задан")
                    response.status_code = 400
                    return response
                stat = repo.get_by_type(args['type'])
                payload = jsonpickle.encode(stat)
                response = app.make_response()
                response.data = payload
                return response
            else:
                response = app.make_response("Недостаточные привилегии для данного запроса")
                response.status_code = 403
                return response
        response = app.make_response("Не предоставлен токен при совершении запроса")
        response.status_code = 403
        return response

    def post(self):
        if 'token' in request.cookies:
            result = check_value(current_config.TRUSTED_SERVICE)
            if result:
                payload = jsonpickle.decode(flask.request.data)
                repo.create(payload["type"], payload["data"])
                response = app.make_response("OK")
                response.status_code = 200
                return response
            else:
                response = app.make_response("Предоставленный токен не является валидным")
                response.status_code = 403
                return response
        response = app.make_response("Не предоставлен токен при совершении запроса")
        response.status_code = 403
        return response

