from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class AoA_1(Resource):
    def post(self):
        response = request.get_json()
        Cn = response['Cn']
        Cna = response['Cna']
        result = Cn / Cna
        return {'val': result}
