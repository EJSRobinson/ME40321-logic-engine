import constants as constants
import math
import numpy as np


def temperatureAtAltitude(Tsl, alt):
    ratio = (288 - 1.983 * (alt / 304.8)) / 288
    return Tsl * ratio

# Get density at altiude, altiude is in meters


def densityAtAltiude(alt):
    ratio = math.e**(-0.0296 * alt / 304.8)
    base = 1.225
    return base * ratio

def pressureAtAltiude(Tsl, alt):
    T = temperatureAtAltitude(Tsl, alt)
    T_imp = 1.8*(T-273) + 32
    P_imp = 2116 * ((T_imp + 459.7)/518.6)**5.256
    P = 47.88 * P_imp
    return P


def dynamicViscosity(Tsl, alt):
    t = temperatureAtAltitude(Tsl, alt)
    temps = [175, 200, 225, 250, 275, 300, 325, 350]
    viscs = [1.182 * 10**(-5), 1.329 * 10**(-5), 1.467 * 10**(-5), 1.599 * 10**(-5), 1.725 * 10 **
             (-5), 1.846 * 10**(-5), 1.962 * 10**(-5), 2.075 * 10**(-5)]
    return np.interp(t, temps, viscs)


def calcDrag(S, cr, TEsw, t, LEsw, Afin, Cbar, Msw, Aref, Ta, Alt, M, AoA, Rs, Arf, Cn):
    AR = S**2 / Afin

    # Velocity
    Talt = temperatureAtAltitude(Ta, Alt)
    a = (constants.gamma * constants.R * Talt)**(1/2)
    V = M * a

    Dref = (4 * Aref / math.pi)**(1/2)

    # Viscosity
    visc = dynamicViscosity(Ta, Alt)

    # Desnity
    RowA = densityAtAltiude(Alt)

    # Reynolds No.
    Re = RowA * V * Dref / visc

    # LE Radius
    rle = t/2

    # Critical Reynolds Number
    ReCrit = 51 * (Rs / Dref)**(-1.039)

    # Skin Friciton
    if (Re < 10 ^ 4):
        Cf = 1/((3.46 * math.log10(10**4) - 5.6)**2)
    elif (Re > 10 ^ 4) and (Re < ReCrit):
        Cf = 1/((3.46 * math.log10(Re) - 5.6)**2)
    else:
        Cf = 0.032 * (Rs/Dref)**0.2

    # Compressible Skin Friction
    if (M > 0.3):
        Cfc = Cf
    else:
        if (Re < ReCrit):
            Cfc = Cf * (1-0.09*(M**2))
        else:
            Cfc = Cf * (1-0.12*(M**2))

    # -> Skin Friction Drag
    Cd_sf = 2*Cfc*(1+2*t/Cbar) * (Afin / Aref)

    # LE Drag

    Cd_Cyl = (1 - M**2)**(-0.417) - 1
    if (Arf == 'flatPlate'):

        Cd_LE = 0.85 * (1 + (M**2)/4 + (M**4)/40)
    elif (Arf == 'flatPlateF'):
        Cd_LE = 2 * (S * rle / Aref) * (math.cos(LEsw))**2 * Cd_Cyl

    # TE Drag
    Cfb = 2 * Cfc * cr / t

    if (Re < ReCrit):
        CfcStar = Cf * (1-0.09)
    else:
        CfcStar = Cf * (1-0.12)

    Kte = ((0.2232 + 4.018*CfcStar)**2) / \
        (((cr/t) * CfcStar)**(2/3)) + (math.cos(Msw))**2

    Afin_TE = S * math.cos(TEsw) * t + Afin * math.sin(AoA)

    Cd_TE = 0.135 * (Afin_TE / Aref) / ((Cfb**(1/3)) *
                                        ((Kte - (M**2) * (math.cos(Msw))**2)**(1/2)))

    # Thickness Drag
    zi = AR * (t/cr)*(1/3)
    Cdtt = 1.15*((t/cr)**(5/3)) * (1.61 + zi -
                                   ((zi - 1.43)**2 + 0.578)**(1/2))
    Kt = (((Cdtt/CfcStar) * (Aref / Afin) - 4*(t/cr)*math.cos(Msw)) /
          (120 * ((t/cr)**4) * (math.cos(Msw))**2))**(2/3) + (math.cos(Msw))**2
    
    print(Kt)

    Cd_thick = 4 * Cfc * (Afin / Aref) * ((t/cr) * math.cos(Msw)) + (
        40 * ((t/cr)**4) * (math.cos(Msw))**2)/((Kt - (M * math.cos(Msw))**2)**(3/2))
    
    print(Cd_thick)

    delt = 0
    Cd_v = Cn**2 * (1 + delt) / (math.pi * AR)

    Cd_thick = 0
    Cd = Cd_sf + Cd_LE + Cd_TE + Cd_thick + Cd_v
    return Cd


def calcMsw(ct, cr, S, LEsw):
    Xsw = 0.5 * (ct - cr) + S*math.tan(LEsw)
    result = math.pi/2 - math.atan(S/Xsw)
    return result


def calcCbar(cr, ct):
    result = ((2/3)*((cr**2 + ct**2 + cr*ct)/(cr + ct)))
    return result
