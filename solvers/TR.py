from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class TR_1(Resource):
    def post(self):
        response = request.get_json()
        AR = response['AR']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        x = (AR/2)*(math.tan(TEsw) + math.tan(LEsw))
        result = (1-x)/(1+x)
        return {'val': result}


class TR_2(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        result = ct/cr
        return {'val': result}
