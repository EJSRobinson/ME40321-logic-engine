from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class TEsw_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        LEsw = response['LEsw']
        S = response['S']
        result = math.atan((cr-ct)/S - math.tan(LEsw))
        return {'val': result}


class TEsw_2(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        TR = response['TR']
        LEsw = response['LEsw']
        S = response['S']
        ct = cr*TR
        result = math.atan((cr-ct)/S - math.tan(LEsw))
        return {'val': result}


class TEsw_3(Resource):
    def post(self):
        response = request.get_json()
        ct = response['ct']
        TR = response['TR']
        LEsw = response['LEsw']
        S = response['S']
        cr = ct / TR
        result = math.atan((cr-ct)/S - math.tan(LEsw))
        return {'val': result}
