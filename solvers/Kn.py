from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Kn_1(Resource):
    def post(self):
        response = request.get_json()
        CnaTot = response['CnaTot']
        Xfin = response['Xfin']
        CnaComp = response['CnaComp']
        Xcomp = response['Xcomp']
        XCog = response['XCog']
        Aref = response['Aref']
        Dref = (4*Aref/math.pi)**(1/2)
        Xall = (1/(CnaTot + CnaComp))*(Xfin * CnaTot + Xcomp * CnaComp)
        result = (Xall - XCog)/Dref
        return {'val': result}
