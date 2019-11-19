import numpy as np
def num_int(f, a, b, n, rule="left"):
    """numerical integration by left-endpoint rule
    f must be a function that works on numpy arrays
    a: left 
    b: right
    n: number of segments"""
    dx = (b-a)/n
    x = np.arange(a, b, step = dx)
    right_y = np.zeros(len(x))
    ## right_x = np.arange(dx,b+dx, step=dx)
    right_x = x + dx
    mid_x = x + dx/2
    if rule=="left":
        y = f(x)
        answer = y.sum() * dx
    elif rule=="simpson":
        left_y = f(x)
        ## right_y = np.array(list(left_y[1:]).append(f(b)))
        right_y[:-1] = left_y[1:]
        right_y[-1] = f(b)
        print(type(right_y))
        mid_y = f(mid_x)
        answer = (left_y + 4*mid_y + right_y).sum()/6*dx
    return answer

def adapt_numint(f,a,b,n0,tol=1e-6):
    intval = num_int(f,a,b,n0)
    nextval = num_int(f,a,b,2*n0)
    while abs(nextval-intval)>tol:
        intval = nextval
        n0 = 2*n0
        nextval = num_int(f,a,b,2*n0)
    return nextval

        ## double the number of steps
        ## compute the next value

def x_squared(x):
    return(x**2)

import math
def math_sin(x):
    return(math.sin(x))

num_int(x_squared,0,1,10)
num_int(x_squared,0,1,n=20)
num_int(x_squared,0,1,n=10**6)

num_int(math_sin, 0, math.pi, 100)
a = np.arange(6)
a**2
a+5
math.sin(a)
np.sin(a)

adapt_numint(x_squared,0,1,n0=10,tol=1e-6)
adapt_numint(x_squared,0,1,n0=10,tol=1e-7)
adapt_numint(x_squared,0,1,n0=10,tol=1e-8)

adapt_numint(x_squared,0,1,n0=10,tol=1e-9)



num_int(x_squared,0,1,n=10**6)
num_int(x_squared,0,1,n=10**6,rule="simpson")

from sympy import *
y = symbol("y")

###
from sympy import *
x = Symbol("x")
type(x)
integrate(x**2,x)
a = Symbol("a")
b = Symbol("b")
integrate(x**2,(x,a,b))
integrate(x**2,(x,0,1))
integrate(log(x)**x,x)

integrate(sqrt(1-x**2),x)
integrate(sqrt(1-x**2),(x,0,1))

a = np.array([1,2,3])  ## np.arange(1,4); 1 + np.arange(3)
import math
np.sqrt(a)
math.sqrt(a)
res = []
for x in a:
    res.append(math.sqrt(x))
print(res)

def arc(x):
    return np.sqrt(1-x**2)

r = num_int(arc, 0, 1, 100000, rule="simpson")
r*4/math.pi


import matplotlib.pyplot as plt
import numpy.random as npr
x = np.linspace(0,1,101)  ## alternative to np.arange()
y = np.sqrt(1-x**2)
fig, ax = plt.subplots()
ax.plot(x,y)
fig.show()
xr = npr.uniform(size=200)
yr = npr.uniform(size=200)
incirc = xr**2+yr**2<1
plt.plot(xr[incirc],yr[incirc],"b-*")
plt.plot(xr[np.logical_not(incirc)],yr[np.logical_not(incirc)],"r-*")