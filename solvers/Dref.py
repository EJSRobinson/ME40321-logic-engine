from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Dref_1(Resource):
    def post(self):
        response = request.get_json()
        Aref = response['Aref']
        result = (4 * Aref / math.pi)**(1/2)
        return {'val': result}
