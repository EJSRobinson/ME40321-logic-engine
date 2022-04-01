from flask_restful import reqparse, Resource
from flask import request
import common as common

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class RowA_1(Resource):
    def post(self):
        response = request.get_json()
        Alt = response['Alt']
        result = common.densityAtAltiude(Alt)
        return {'val': result}
