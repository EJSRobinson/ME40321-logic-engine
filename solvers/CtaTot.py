from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class CtaTot_1(Resource):
    def post(self):
        response = request.get_json()
        Cta = response['Cta']
        N = response['N']
        result = Cta * N
        return {'val': result}
