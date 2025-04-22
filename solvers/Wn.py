from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Wn_1(Resource):
    def post(self):
        response = request.get_json()
        C1 = response['C1']
        I = response['I']
        result = (C1 / I)**(1/2)
        return {'val': result}
