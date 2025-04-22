from flask_restful import reqparse, Resource
from flask import request

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Fl_1(Resource):
    def post(self):
        response = request.get_json()
        Cl = response['Cl']
        Aref = response['Aref']
        V = response['V']
        RowA = response['RowA']
        result = 0.5 * RowA * V * V * Aref * Cl
        return {'val': result}
