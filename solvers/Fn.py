from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Fn_1(Resource):
    def post(self):
        response = request.get_json()
        Cn = response['Cn']
        Aref = response['Aref']
        V = response['V']
        RowA = response['RowA']
        result = 0.5 * RowA * V * V * Aref * Cn
        return {'val': result}
