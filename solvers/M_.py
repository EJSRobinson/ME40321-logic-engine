from flask_restful import reqparse, Resource
from flask import request
import psa.standard as standard
import constants as constants

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class M_1(Resource):
    def post(self):
        response = request.get_json()
        V = response['V']
        Ta = response['Ta']
        Alt = response['Alt']
        t = Ta * standard.atmosphere(Alt/1000)[2]

        a = (constants.gamma * constants.R * t)**(1/2)
        result = V / a
        return {'val': result}
