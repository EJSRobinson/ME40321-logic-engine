from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Ct_1(Resource):
    def post(self):
        response = request.get_json()
        AoA = response['AoA']
        Cna = response['Cta']
        result = AoA * Cna
        return {'val': result}
