from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Msw_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        S = response['S']
        LEsw = response['LEsw']
        Xsw = 0.5 * (ct - cr) + S*math.tan(LEsw)
        result = math.pi/2 - math.atan(S/Xsw)
        return {'val': result}
