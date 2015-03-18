import numpy as np
## import scipy.integrate as scint
import numpy.random as rand

def int1(f,a,b,n):
    '''integrate a function that takes an array argument'''
    x = np.linspace(a,b,n,endpoint=False)
    delta = (b-a)/n
    y = f(x)
    return(y.sum()*delta)

def int2(f,a,b,n):
    '''integrate a function by brute force'''
    s = 0
    c = a
    delta = (b-a)/n
    for r in range(n):
        s += f(c)
        c += delta
    return(s*delta)        

## use scipy.integrate after it is called in ...

def intmc(f,a,b,n,maxval=1):
    x = a+(b-a)*rand.rand(n)
    y = f(x)
    yrand = rand.rand(n)*maxval
    frac = (yrand<y).sum()/n
    return((b-a)*frac)

def f1(a):
    return(np.sin(a))

## print(int1(f1,0,np.pi,1001))
## print(int2(f1,0,np.pi,1001))
## print(intmc(f1,0,np.pi,1e6))
    
