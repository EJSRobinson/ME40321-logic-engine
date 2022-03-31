
import solvers.common as common
import math

S = 0.01
cr = 0.01
LEsw = 0.6


ct = 0.007
Afin = 0.5 * (cr + ct) * S

Xsw = 0.5 * (ct - cr) + S*math.tan(LEsw)

result = math.pi/2 - math.atan(S/Xsw)

print(result)
