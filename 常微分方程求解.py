from sympy import *
y= symbols('y',cls=Function)
x= symbols ('x')
eq=Eq(y(x).diff(x,2)+2*y(x).diff(x,1)+y(x),x**2)
print(dsolve(eq,y(x)))



