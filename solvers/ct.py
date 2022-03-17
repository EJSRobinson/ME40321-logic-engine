from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class ct_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        A = response['Afin']
        S = response['S']
        result = 2*A/S - cr
        return {'Result': result}
