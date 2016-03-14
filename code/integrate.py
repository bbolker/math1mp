import numpy as np
## import scipy.integrate as scint
import numpy.random as rand

def int_brute(f,a,b,n):
    """integrate a function by brute force
    f: function
    a: lower limit
    b: upper limit
    n: number of partitions
    """
    
    s = 0
    c = a
    delta = (b-a)/n
    for r in range(n):
        s += f(c)
        c += delta
    return(s*delta)        

def int_array(f,a,b,n):
    '''integrate a function that takes an array argument'''
    x = np.linspace(a,b,n,endpoint=False)
    delta = (b-a)/n
    y = f(x)
    return(y.sum()*delta)

def int_trap(f,a,b,n):
    """trapezoid rule"""
    x = np.linspace(a,b,n+1,endpoint=True)
    delta = (b-a)/n
    v = f(x)
    y = (v[1:]+v[:-1])/2.0
    return(y.sum()*delta)

## use scipy.integrate after it is called in ...

def intmc(f,a,b,n,maxval=1):
    x = a+(b-a)*rand.rand(n)
    y = f(x)
    yrand = rand.rand(n)*maxval
    frac = (yrand<y).sum()/n
    return((b-a)*frac)

def f1(x):
    return(np.sqrt(1-x**2))

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    print(int_brute(f1,0,1,101)*4)
    print(int_array(f1,0,1,101)*4)
    print(int_trap(f1,0,1,101)*4)
    print(int_array(f1,0,1,501)*4)
    print(intmc(f1,0,1,1e6)*4)
    
    
    
