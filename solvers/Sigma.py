from flask_restful import reqparse, Resource
from flask import request
import math
import exporters as exportFuncs
import numpy as np

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Sigma_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        TEsw = response['TEsw']
        LEsw = response['LEsw']
        t = response['t']
        S = response['S']
        steps = 100
        stress = exportFuncs.calcStress(cr, Fn, Afin, TEsw, LEsw, S, t ,steps)
        result = np.amax(stress)
        return {'val': result}
