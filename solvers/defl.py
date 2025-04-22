from flask_restful import reqparse, Resource
from flask import request
import math
import exporters as exportFuncs
import numpy as np

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class defl_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        t = response['t']
        S = response['S']
        E = response['Mat']['E']
        steps = 100
        defl = exportFuncs.calcDeflection(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t)
        result = np.amax(defl)
        return {'val': result}
