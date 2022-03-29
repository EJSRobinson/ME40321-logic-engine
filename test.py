
import math

Dref = 0.15
Cna = 3.251
TR = 0.5
AR = 2
TEsw = 0
Afin = 0.05

err = 100

while err > 0.000001:
    cr = 2 * Afin**(1/2) / ((1+TR) * AR**(1/2))
    LEsw = math.atan(cr*(1-TR)/((Afin * AR)**(1/2)) - math.tan(TEsw))
    lfx = (cr/2) * (TR - 1) + (Afin * AR)**(1/2) * math.tan(LEsw)
    lf = (lfx**2 + Afin*AR)**(1/2)
    Block1 = (1 + (Dref/2)/((Afin * AR)**(1/2) + Dref/2))**(-1)
    Block2 = ((4/Dref**2 * AR)/(1+(1+(2*lf/(cr*(1+TR)))**2)**(1/2)))**(-1)
    AfinNew = Cna * Block1 * Block2
    err = abs(Afin - AfinNew)
    Afin = AfinNew

print('Final Afin: '+str(Afin))
print('Final Cr: '+str(cr))
