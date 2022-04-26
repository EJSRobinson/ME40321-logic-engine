from flask_restful import reqparse, Resource
from flask import request, Response
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import constants
import common
import math

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)

def c(LEsw, TEsw, cr, S):
    return (cr - S * math.tan(LEsw) - S *math.tan(TEsw))

def I(c, t):
    return (t * c**3) / 12

def calcSpanVector(S, steps):
    S_vect = np.arange(0, S, S/steps)
    S_cent = []
    for i in range((len(S_vect) - 1)):
        s = 0.5 * (S_vect[i] + S_vect[i+1])
        S_cent.append(s * 1000)
    return np.asarray(S_cent)
    
def calcShearForce(cr, Fn, Afin, TEsw, LEsw, S ,steps):
    Fna = Fn / Afin
    S_vect = np.arange(0, S, S/steps)
    S_strip = S / steps
    Fn_vect = []
    for i in range((len(S_vect) - 1)):
        a = (c(LEsw, TEsw, cr, S_vect[i]) + c(LEsw, TEsw, cr, S_vect[i + 1])) * 0.5 * S_strip
        Fn_vect.append(a * Fna)
    return np.asarray(Fn_vect)

def calcBendingMoment(cr, Fn, Afin, TEsw, LEsw, S ,steps):
    sf = calcShearForce(cr, Fn, Afin, TEsw, LEsw, S ,steps)
    span = calcSpanVector(S, steps)
    # moment = np.multiply(sf, span)
    moment = sf
    bm = []
    for i in range(len(moment)):
        result = 0
        for j in range(i, len(moment)):
            result += moment[j]
        bm.append(result)
    return np.asarray(bm)

def calcDeflectionAngle(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t):
    bm = calcBendingMoment(cr, Fn, Afin, TEsw, LEsw, S ,steps)
    span = calcSpanVector(S, steps)
    angle_change = []
    for i in range(len(bm)):
        angle_change.append(bm[i] * span[i] / (E * I(c(LEsw, TEsw, cr, span[i]), t)))
    angle = []
    for i in range(len(angle_change)):
        result = 0
        for j in range(0, i):
            result += angle_change[j]
        angle.append(result)
    return np.asarray(angle)

def calcDeflection(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t):
    angle = calcDeflectionAngle(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t)
    span = calcSpanVector(S, steps)
    def_change = []
    for i in range(len(angle)):
        def_change.append(angle[i] * span[i])
    delection = []
    for i in range(len(def_change)):
        result = 0
        for j in range(0, i):
            result += def_change[j]
        delection.append(result)
    return np.asarray(delection)

class Fn_V(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        Cn = response['Cn']
        Vmax = response['V']
        Alt = response['Alt']
        Vmin = 0
        RowA_SL = response['RowA']
        RowA_Alt = common.densityAtAltiude(Alt)
        Aref = response['Aref']
        V = np.arange(Vmin, Vmax, 1)
        Fn_SL = 0.5 * Cn * RowA_SL * Aref * V**2
        Fn_Alt = 0.5 * Cn * RowA_Alt * Aref * V**2
        plt.plot(V, Fn_SL, label='Ground Level')
        plt.plot(V, Fn_Alt, label='Maximum Altitude')
        plt.legend(loc='upper left')
        plt.xlabel('Velocity (m/s)')
        plt.ylabel('Normal Force (N)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

class Fn_M(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        Cn = response['Cn']
        T_SL = response['Ta']
        Alt = response['Alt']
        T_Alt = common.temperatureAtAltitude(T_SL, Alt)
        Mmax = response['M']
        Mmin = 0
        RowA_SL = response['RowA']
        RowA_Alt = common.densityAtAltiude(Alt)
        Aref = response['Aref']
        M = np.arange(Mmin, Mmax, 0.01)
        SoS_SL = (constants.gamma * constants.R * T_SL)**(1/2)
        Fn_SL = 0.5 * Cn * RowA_SL * Aref * (M * SoS_SL)**2
        SoS_Alt = (constants.gamma * constants.R * T_Alt)**(1/2)
        Fn_Alt = 0.5 * Cn * RowA_Alt * Aref * (M * SoS_Alt)**2
        plt.clf()
        plt.plot(M, Fn_SL, label='Ground Level')
        plt.plot(M, Fn_Alt, label='Maximum Altitude')
        plt.legend(loc='upper left')
        plt.xlabel('Mach Number')
        plt.ylabel('Normal Force (N)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

class Fn_AoA(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        Cna = response['Cna']
        AoAmax = response['AoA']
        AoAmin = 0
        V = response['V']
        Alt = response['Alt']
        RowA_SL = response['RowA']
        RowA_Alt = common.densityAtAltiude(Alt)
        Aref = response['Aref']
        AoA = np.arange(AoAmin, AoAmax, 0.001)
        Cn = AoA * Cna
        Fn_SL = 0.5 * Cn * RowA_SL * Aref * V**2
        Fn_Alt = 0.5 * Cn * RowA_Alt * Aref * V**2
        AoA = AoA * 180 / math.pi
        plt.clf()
        plt.plot(AoA, Fn_SL, label='Ground Level')
        plt.plot(AoA, Fn_Alt, label='Maximum Altitude')
        plt.legend(loc='upper left')
        plt.xlabel('Angle of Attack (°)')
        plt.ylabel('Normal Force (N)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

class Fn_S(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        S = response['S']
        steps = 100
        plt.clf()
        plt.plot(calcSpanVector(S, steps), calcShearForce(cr, Fn, Afin, TEsw, LEsw, S ,steps))
        plt.xlabel('Span (mm)')
        plt.ylabel('Normal Force (N)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

class BM_S(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        S = response['S']
        steps = 100
        plt.clf()
        plt.plot(calcSpanVector(S, steps), calcBendingMoment(cr, Fn, Afin, TEsw, LEsw, S ,steps))
        plt.xlabel('Span (mm)')
        plt.ylabel('Bending Moment (Nm)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

class Ang_S(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        E = response['Mat']['E']
        t = response['t']
        S = response['S']
        steps = 300
        plt.clf()
        plt.plot(calcSpanVector(S, steps), calcDeflectionAngle(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t) * (180 / math.pi))
        plt.xlabel('Span (mm)')
        plt.ylabel('Deflection Angle (°)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

class Defl_S(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        E = response['Mat']['E']
        t = response['t']
        S = response['S']
        steps = 100
        plt.clf()
        plt.plot(calcSpanVector(S, steps), calcDeflection(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t) * 1000)
        plt.xlabel('Span (mm)')
        plt.ylabel('Deflection (mm)')
        plt.savefig(f, format = "png")
        return Response(f.getvalue(), mimetype='image/png')

# ---------------------

class Fn_V_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        Cn = response['Cn']
        Vmax = response['V']
        Alt = response['Alt']
        Vmin = 0
        RowA_SL = response['RowA']
        RowA_Alt = common.densityAtAltiude(Alt)
        Aref = response['Aref']
        V = np.arange(Vmin, Vmax, 1)
        Fn_SL = 0.5 * Cn * RowA_SL * Aref * V**2
        Fn_Alt = 0.5 * Cn * RowA_Alt * Aref * V**2
        return {'val': [V, Fn_SL, Fn_Alt]}

class Fn_M_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        Cn = response['Cn']
        T_SL = response['Ta']
        Alt = response['Alt']
        T_Alt = common.temperatureAtAltitude(T_SL, Alt)
        Mmax = response['M']
        Mmin = 0
        RowA_SL = response['RowA']
        RowA_Alt = common.densityAtAltiude(Alt)
        Aref = response['Aref']
        M = np.arange(Mmin, Mmax, 0.01)
        SoS_SL = (constants.gamma * constants.R * T_SL)**(1/2)
        Fn_SL = 0.5 * Cn * RowA_SL * Aref * (M * SoS_SL)**2
        SoS_Alt = (constants.gamma * constants.R * T_Alt)**(1/2)
        Fn_Alt = 0.5 * Cn * RowA_Alt * Aref * (M * SoS_Alt)**2
        return {'val': [M, Fn_SL, Fn_Alt]}

class Fn_AoA_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        Cna = response['Cna']
        AoAmax = response['AoA']
        AoAmin = 0
        V = response['V']
        Alt = response['Alt']
        RowA_SL = response['RowA']
        RowA_Alt = common.densityAtAltiude(Alt)
        Aref = response['Aref']
        AoA = np.arange(AoAmin, AoAmax, 0.001)
        Cn = AoA * Cna
        Fn_SL = 0.5 * Cn * RowA_SL * Aref * V**2
        Fn_Alt = 0.5 * Cn * RowA_Alt * Aref * V**2
        AoA = AoA * 180 / math.pi
        return {'val': [V, Fn_SL, Fn_Alt]}

class Fn_S_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        S = response['S']
        steps = 100
        return {'val': [calcSpanVector(S, steps), calcShearForce(cr, Fn, Afin, TEsw, LEsw, S ,steps)]}

class BM_S_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        S = response['S']
        steps = 100
        return {'val': [calcSpanVector(S, steps), calcBendingMoment(cr, Fn, Afin, TEsw, LEsw, S ,steps)]}

class Ang_S_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        E = response['Mat']['E']
        t = response['t']
        S = response['S']
        steps = 300
        return {'val': [calcSpanVector(S, steps), calcDeflectionAngle(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t) * (180 / math.pi)]}

class Defl_S_data(Resource):
    def post(self):
        response = request.get_json()
        f = io.BytesIO()
        cr = response['cr']
        Fn = response['Fn']
        Afin = response['Afin']
        LEsw = response['LEsw']
        TEsw = response['TEsw']
        E = response['Mat']['E']
        t = response['t']
        S = response['S']
        steps = 100
        return {'val': [calcSpanVector(S, steps).tolist(), (calcDeflection(cr, Fn, Afin, TEsw, LEsw, S ,steps, E, t) * 1000).tolist()]}