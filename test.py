
import solvers.common as common
import math

S = 0.01
cr = 0.01
LEsw = 0.524
TEsw = 0


Ws = math.tan(LEsw) + math.tan(TEsw)
ct = cr - S*Ws
Afin = 0.5 * (cr + ct) * S

c_ = (2/3)*((cr ** 2 + ct ** 2 + cr*ct)/(cr + ct))

# v = (2/Afin) * S * ((Ws * S**2 / 3) - (cr * Ws * S) + (cr**2))
print(c_)
