from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Cna_1(Resource):
    def post(self):
        response = request.get_json()
        Kn = response['Kn']
        Xfin = response['Xfin']
        XCog = response['XCog']
        N = response['N']
        CnaComp = response['CnaComp']
        Xcomp = response['Xcomp']
        Aref = response['Aref']

        Dref = (4*Aref/math.pi)**(1/2)  # Reference Length
        Xcp = XCog + Kn*Dref    # Overall Cp
        CnaTot = CnaComp * (Xcomp - Xcp) / (Xcp - Xfin)  # Single Fin
        result = CnaTot / N
        return {'val': result}



class Cna_2(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        S = response['S']
        LEsw = response['LEsw']
        Aref = response['Aref']

        Dref = (4*Aref/math.pi)**(1/2)
        Xr = S * math.tan(LEsw)
        Xlf = ct/2 + Xr - cr/2
        Lf = (Xlf**2 + S**2)**(1/2)

        result = (1 + Dref/(S + Dref)) * (4*((S/Dref)**2)) / \
            (1 + (1 + (2 * Lf / (cr + ct))**2)**(1/2))
        return {'val': result}


class Cna_3(Resource):
    def post(self):
        response = request.get_json()
        Cn = response['Cn']
        AoA = response['AoA']
        result = Cn / AoA
        return {'val': result}
