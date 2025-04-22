from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class LEsw_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        TEsw = response['TEsw']
        S = response['S']
        result = math.atan((cr-ct)/S - math.tan(TEsw))
        return {'val': result}


class LEsw_2(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        TR = response['TR']
        TEsw = response['TEsw']
        S = response['S']
        ct = cr*TR
        result = math.atan((cr-ct)/S - math.tan(TEsw))
        return {'val': result}


class LEsw_3(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        TR = response['TR']
        TEsw = response['TEsw']
        S = response['S']
        cr = ct / TR
        result = math.atan((cr-ct)/S - math.tan(TEsw))
        return {'val': result}
