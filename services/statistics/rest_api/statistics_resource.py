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
                payload

    def post(self):
        if 'token' in request.cookies:
            result = check_value(current_config.TRUSTED_SERVICE)
            if result:
                payload = jsonpickle.decode(flask.request.data)
                repo.create(payload["type"], payload["data"])
                response = app.make_response("")
                response.status_code = 200
                response.data = jsonpickle.encode()
            else:
                response = app.make_response("The token is not valid")
                response.status_code = 403
                return response
        response = app.make_response("No valid token supplied")
        response.status_code = 403
        return response

