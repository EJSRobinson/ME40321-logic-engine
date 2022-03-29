from flask_restful import reqparse, Resource
from flask import request
import solvers.common as common
import solvers.constants as constants

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Mach_1(Resource):
    def post(self):
        response = request.get_json()
        V = response['V']
        Ta = response['Ta']
        Alt = response['Alt']
        Talt = common.temperatureAtAltitude(Ta, Alt)

        a = (constants.gamma * constants.R * Talt)**(1/2)
        result = V / a
        return {'val': result}
