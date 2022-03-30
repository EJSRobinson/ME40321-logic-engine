import math
import numpy as np

# Get Temperature at altitude, altiude is in meters


def temperatureAtAltitude(Tsl, alt):
    ratio = (288 - 1.983 * (alt / 304.8)) / 288
    return Tsl * ratio

# Get density at altiude, altiude is in meters


def densityAtAltiude(alt):
    ratio = math.e**(-0.0296 * alt / 304.8)
    base = 1.225
    return base * ratio


def dynamicViscosity(Tsl, alt):
    t = temperatureAtAltitude(Tsl, alt)
    temps = [175, 200, 225, 250, 275, 300, 325, 350]
    viscs = [1.182 * 10**(-5), 1.329 * 10**(-5), 1.467 * 10**(-5), 1.599 * 10**(-5), 1.725 * 10 **
             (-5), 1.846 * 10**(-5), 1.962 * 10**(-5), 2.075 * 10**(-5)]
    return np.interp(t, temps, viscs)
