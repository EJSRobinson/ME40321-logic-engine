from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class N_1(Resource):
    def post(self):
        response = request.get_json()
        mT = response['mT']
        m = response['m']
        result = mT / m
        return {'val': result}
