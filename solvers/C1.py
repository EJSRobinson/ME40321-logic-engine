from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class C1_1(Resource):
    def post(self):
        response = request.get_json()
        Aref = response['Aref']
        V = response['V']
        RowA = response['RowA']
        Cna = response['Cna']
        Kn = response['Kn']
        result = RowA * Aref * Kn * 0.5 * Cna * V**2
        return {'val': result}
