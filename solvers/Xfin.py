from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Xfin_1(Resource):
    def post(self):
        response = request.get_json()
        CnaTot = response['CnaTot']
        Kn = response['Kn']
        CnaComp = response['CnaComp']
        Xcomp = response['Xcomp']
        XCog = response['XCog']
        Aref = response['Aref']
        Dref = (4*Aref/math.pi)**(1/2)
        Xcp = Kn * Dref + Xcog
        result = (1/CnaTot) * (Xcp*(CnaComp + CnaTot) - Xcomp * CnaComp)
        return {'val': result}
