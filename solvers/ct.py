from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class ct_1(Resource):
    def post(self):
        response = request.get_json()
        result = response['var1'] * response['var2'] * response['var3']
        return {'Result': result}
