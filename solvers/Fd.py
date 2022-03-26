from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Fd_1(Resource):
    def post(self):
        response = request.get_json()
        Cd = response['Cd']
        Aref = response['Aref']
        V = response['V']
        RowA = response['RowA']
        result = 0.5 * RowA * V * V * Aref * Cd
        return {'val': result}
