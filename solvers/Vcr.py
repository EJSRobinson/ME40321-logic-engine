from flask_restful import reqparse, Resource
from flask import request
import math
import numpy as np
import common as common
import constants as constants

parser = reqparse.RequestParser()
parser.add_argument('vars', type=str)


class Vcr_1(Resource):
    def post(self):
        response = request.get_json()
        cr = response['cr']
        TR = response['TR']
        AR = response['AR']
        Ta = response['Ta']
        Alt = response['Alt']
        t = response['t']
        G = response['Mat']['G']
        temp = common.temperatureAtAltitude(Ta, Alt)
        Pres = common.pressureAtAltiude(Ta, Alt)
        Pres_imp = Pres / 47.88
        SoS = (constants.gamma * constants.R * temp)**(1/2)
        SoS_imp = SoS * 3.281
        G_imp = G / 6857.1
        Vcr_imp = SoS_imp * (G_imp/((1.337*AR**3 * Pres_imp * (TR + 1))/(2*(AR+2)*(t/cr)**3)))**(1/2)
        Vcr = Vcr_imp / 3.281
        result = Vcr
        return {'val': result}
