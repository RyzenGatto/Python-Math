import math
from sympy import *


x = symbols('x')

pi = math.pi

function = (30*sin(2*pi*60*x) + 40*sin(2*pi*120*x))**2

r = integrate(function)

F1 = r.subs(x, 0)
F2 = r.subs(x, math.pi)

Fund = F2 - F1

AVG = Fund/math.pi

FDM = math.sqrt(AVG)

print(F1, F2, Fund, FDM)