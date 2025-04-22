from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Zeta_1(Resource):
    def post(self):
        response = request.get_json()
        C1 = response['C1']
        C2 = response['C2']
        I = response['I']
        result = C2 / (2 * (C1 * I)**(1/2))
        return {'val': result}
