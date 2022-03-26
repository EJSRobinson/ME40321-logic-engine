from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class m_1(Resource):
    def post(self):
        response = request.get_json()
        mT = response['mT']
        N = response['N']
        result = mT / N
        return {'val': result}


class m_2(Resource):
    def post(self):
        response = request.get_json()
        Afin = response['Afin']
        t = response['t']
        rowM = response['Mat']
        result = Afin * t * rowM
        return {'val': result}
