from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Aref_1(Resource):
    def post(self):
        response = request.get_json()
        Dref = response['Dref']
        result = math.pi * Dref**2 / 4
        return {'val': result}
