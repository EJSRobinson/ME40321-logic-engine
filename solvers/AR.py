from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class AR_1(Resource):
    def post(self):
        response = request.get_json()
        S = response['S']
        A = response['Afin']
        result = (S**2)/A
        return {'val': result}


class AR_2(Resource):
    def post(self):
        response = request.get_json()
        TR = response['TR']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        result = 2*((1-TR)/(1+TR))/(math.tan(TEsw) + math.tan(LEsw))
        return {'val': result}
