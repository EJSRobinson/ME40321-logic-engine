from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Tp_1(Resource):
    def post(self):
        response = request.get_json()
        Wn = response['Wn']
        freq = Wn / (2 * math.pi)
        result = 1 / freq
        return {'val': result}
