from flask_restful import reqparse, Resource
from flask import request
import common as common

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Msw_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        S = response['S']
        LEsw = response['LEsw']
        result = common.calcMsw(ct, cr, S, LEsw)
        return {'val': result}
