from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Cl_1(Resource):
    def post(self):
        response = request.get_json()
        AoA = response['AoA']
        Cn = response['Cn']
        Ct = response['Ct']
        result = Cn * math.cos(AoA) - Ct * math.sin(AoA)
        return {'val': result}
