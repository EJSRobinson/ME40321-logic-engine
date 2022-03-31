from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Cbar_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        result = (2/3)*((cr ** 2 + ct ** 2 + cr*ct)/(cr + ct))
        return {'val': result}
