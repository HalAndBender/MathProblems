#reference: http://www.scipy-lectures.org/advanced/sympy.html#using-sympy-as-a-calculator


from sympy import *
x = Symbol('x')
y = Symbol('y')

print(diff(sin(x), x))
#cos(x)

print(diff(sin(2*x), x))
#2*cos(2*x)

print(diff(tan(x), x))
#1 + tan(x)**2

