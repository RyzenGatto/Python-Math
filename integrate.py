import math
from sympy import *

pi = math.pi
x = symbols('x')

# lower bounds
a =
#upper bounds
b =

#input function + example (for RMS, you must square your original function before integration. This function is squared with **2. Otherwise, remove **2
function = (30*sin(2*pi*60*x) + 40*sin(2*pi*120*x))**2

r = integrate(function)

#Evaluates the antiderivative at 'a' and 'b'
F1 = r.subs(x, a)
F2 = r.subs(x, b)

Fund = F2 - F1

AVG = Fund/(b-a)

RMS = math.sqrt(AVG)

print(F1, F2, Fund, RMS)
