from flask_restful import reqparse, Resource
from flask import request
import math
import numpy as np
import common as common

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class optimiseDrag(Resource):
    def post(self):
        response = request.get_json()
        S_max = response['S']['max']
        S_min = response['S']['min']
        cr_max = response['cr']['max']
        cr_min = response['cr']['min']
        ct_max = response['ct']['max']
        ct_min = response['ct']['min']
        TEsw_max = response['TEsw']['max']
        TEsw_min = response['TEsw']['min']

        t = response['t']        # max
        Aref = response['Aref']  # val
        Ta = response['Ta']      # min
        Alt = response['Alt']    # min
        M = response['M']        # max
        AoA = response['AoA']    # max
        Rs = response['Mat']     # val
        Arf = response['Arf']    # val
        Cn = response['Cn']      # max

        S = np.arange(S_min, S_max, 0.0005)
        cr = np.arange(cr_min, cr_max, 0.0005)
        ct = np.arange(ct_min, ct_max, 0.0005)
        TEsw = np.arange(TEsw_min, TEsw_max, math.pi / 180)

        if (len(S) == 0):
            S = np.array([S_min])
        if (len(cr) == 0):
            cr = np.array([cr])
        if (len(ct) == 0):
            ct = np.array([ct])
        if (len(TEsw) == 0):
            TEsw = np.array([TEsw_min])

        results = np.zeros((len(S), len(cr), len(ct), len(TEsw)))

        for i in range(len(S)):
            for j in range(len(cr)):
                for k in range(len(ct)):
                    for l in range(len(TEsw)):
                        LEsw = math.atan(
                            (cr[j]-ct[k])/S[i] - math.tan(TEsw[l]))
                        Afin = 0.5 * (cr[j] + ct[k]) * S[i]
                        Cbar = common.calcCbar(cr[j], ct[k])
                        Msw = common.calcMsw(ct[k], cr[j], S[i], LEsw)
                        results[i][j][k][l] = common.calcDrag(
                            S[i], cr[j], TEsw[l], t, LEsw, Afin, Cbar, Msw, Aref, Ta, Alt, M, AoA, Rs, Arf, Cn)

        ind = np.unravel_index(np.argmax(results), results.shape)
        S_final = float(S[ind[0]])
        cr_final = float(cr[ind[1]])
        ct_final = float(ct[ind[2]])
        TEsw_final = float(TEsw[ind[3]])
        return {'S': S_final, 'cr': cr_final, 'ct': ct_final, 'TEsw': TEsw_final}
