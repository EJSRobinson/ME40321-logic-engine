from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class cr_1(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        A = response['Afin']
        S = response['S']
        result = 2*A/S - ct
        return {'val': result}


class cr_2(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        S = response['S']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        result = ct + S*(math.tan(TEsw) + math.tan(LEsw))
        return {'val': result}


class cr_3(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        TR = response['TR']
        result = ct / TR
        return {'val': result}


class cr_6(Resource):
    def post(self):
        response = request.get_json()
        Afin = response['Afin']
        TR = response['TR']
        AR = response['AR']
        result = 2 * Afin**(1/2) / ((1 + TR) * AR**(1/2))
        return {'val': result}
