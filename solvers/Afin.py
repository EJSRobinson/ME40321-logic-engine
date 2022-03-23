from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Afin_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        S = response['S']
        result = 0.5 * S * (cr + ct)
        return {'val': result}


class Afin_2(Resource):
    def post(self):
        response = request.get_json()
        AR = response['AR']
        S = response['S']
        result = (S**2)/AR
        return {'val': result}


class Afin_3(Resource):
    def post(self):
        response = request.get_json()
        rowMat = response['Mat']
        t = response['t']
        m = response['m']
        result = m/(rowMat * t)
        return {'val': result}
