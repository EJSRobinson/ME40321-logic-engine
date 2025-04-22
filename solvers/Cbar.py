from flask_restful import reqparse, Resource
from flask import request
import common as common

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Cbar_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        result = common.calcCbar(cr, ct)
        return {'val': result}
