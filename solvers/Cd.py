from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Cd_1(Resource):
    def post(self):
        response = request.get_json()
        AoA = response['AoA']
        Cn = response['Cn']
        Ct = response['Ct']
        result = Ct * math.cos(AoA) + Cn * math.sin(AoA)
        return {'val': result}
