from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class ct_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        A = response['Afin']
        S = response['S']
        result = 2*A/S - cr
        return {'val': result}


class ct_2(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        S = response['S']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        result = cr - S*(math.tan(TEsw) + math.tan(LEsw))
        return {'val': result}


class ct_3(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        TR = response['TR']
        result = cr * TR
        return {'val': result}
