import math

# Get Temperature at altitude, altiude is in meters


def temperatureAtAltitude(Tsl, alt):
    ratio = 288 * 1.983 * (alt / 304.8) / 288
    return Tsl * ratio

# Get density at altiude, altiude is in meters


def densityAtAltiude(alt):
    ratio = math.e**(-0.0296 * alt / 304.8)
    base = 1.225
    return base * ratio
