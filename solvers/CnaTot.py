from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class CnaTot_1(Resource):
    def post(self):
        response = request.get_json()
        Cna = response['Cna']
        N = response['N']
        result = Cna * N
        return {'val': result}
