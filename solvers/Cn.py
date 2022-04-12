from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Cn_1(Resource):
    def post(self):
        response = request.get_json()
        AoA = response['AoA']
        Cna = response['Cna']
        result = AoA * Cna
        return {'val': result}

class Cn_2(Resource):
    def post(self):
        response = request.get_json()
        RowA = response['RowA']
        V = response['V']
        Fn = response['Fn']
        Aref = response['Aref']
        result = Fn / (0.5 * RowA * Aref * V**2)
        return {'val': result}
