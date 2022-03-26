from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class mT_1(Resource):
    def post(self):
        response = request.get_json()
        m = response['mT']
        N = response['N']
        result = m * N
        return {'val': result}
