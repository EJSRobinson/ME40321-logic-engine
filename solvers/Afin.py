from flask_restful import reqparse, Resource
from flask import request
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Afin_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        ct = response['ct']
        S = response['S']
        result = 0.5 * S * (cr + ct)
        return {'val': result}


class Afin_2(Resource):
    def post(self):
        response = request.get_json()
        AR = response['AR']
        S = response['S']
        result = (S**2)/AR
        return {'val': result}


class Afin_3(Resource):
    def post(self):
        response = request.get_json()
        rowMat = response['Mat']
        t = response['t']
        m = response['m']
        result = m/(rowMat * t)
        return {'val': result}


class Afin_4(Resource):
    def post(self):
        response = request.get_json()
        Aref = response['Aref']
        Cna = response['Cna']
        TR = response['TR']
        AR = response['AR']
        TEsw = response['TEsw']
        Dref = (4*Aref / math.pi)**(1/2)

        while err > 0.000001:
            cr = 2 * Afin**(1/2) / ((1+TR) * AR**(1/2))
            LEsw = math.atan(cr*(1-TR)/((Afin * AR)**(1/2)) - math.tan(TEsw))
            lfx = (cr/2) * (TR - 1) + (Afin * AR)**(1/2) * math.tan(LEsw)
            lf = (lfx**2 + Afin*AR)**(1/2)
            Block1 = (1 + (Dref/2)/((Afin * AR)**(1/2) + Dref/2))**(-1)
            Block2 = ((4/Dref**2 * AR) /
                      (1+(1+(2*lf/(cr*(1+TR)))**2)**(1/2)))**(-1)
            AfinNew = Cna * Block1 * Block2
            err = abs(Afin - AfinNew)
            Afin = AfinNew

        result = Afin
        return {'val': result}


class Afin_5(Resource):
    def post(self):
        response = request.get_json()
        Aref = response['Aref']
        Cna = response['Cna']
        TR = response['TR']
        AR = response['AR']
        LEsw = response['LEsw']
        Dref = (4*Aref / math.pi)**(1/2)

        while err > 0.000001:
            cr = 2 * Afin**(1/2) / ((1+TR) * AR**(1/2))
            lfx = (cr/2) * (TR - 1) + (Afin * AR)**(1/2) * math.tan(LEsw)
            lf = (lfx**2 + Afin*AR)**(1/2)
            Block1 = (1 + (Dref/2)/((Afin * AR)**(1/2) + Dref/2))**(-1)
            Block2 = ((4/Dref**2 * AR) /
                      (1+(1+(2*lf/(cr*(1+TR)))**2)**(1/2)))**(-1)
            AfinNew = Cna * Block1 * Block2
            err = abs(Afin - AfinNew)
            Afin = AfinNew

        result = Afin
        return {'val': result}
