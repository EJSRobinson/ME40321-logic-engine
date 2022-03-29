from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class S_1(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        cr = response['cr']
        A = response['Afin']
        result = 2*A/(cr - ct)
        return {'val': result}


class S_2(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        cr = response['cr']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        result = (cr-ct)/(math.tan(TEsw) + math.tan(LEsw))
        return {'val': result}


class S_5(Resource):
    def post(self):
        response = request.get_json()
        Afin = response['Afin']
        AR = response['AR']
        result = (AR*Afin)**(1/2)
        return {'val': result}
