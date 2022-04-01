from flask_restful import reqparse, Resource
from flask import request
import solvers.common as common
import common as common

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Ctang_1(Resource):
    def post(self):
        response = request.get_json()
        Aref = response['Aref']
        Ta = response['Ta']
        Alt = response['Alt']
        M = response['M']
        Afin = response['Afin']
        t = response['t']
        Cbar = response['Cbar']
        S = response['S']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        Msw = response['Msw']
        cr = response['cr']
        AoA = response['AoA']
        Rs = response['Mat']
        Arf = response['Arf']
        Cn = response['Cn']

        Cd = common.calcDrag(S, cr, TEsw, t, LEsw,
                             Afin, Cbar, Msw, Aref, Ta, Alt, M, AoA, Rs, Arf, Cn)

        return {'val': Cd}
