from math import pi,factorial

def sin_series1(x,tol=1e-6,maxit=100):
    """Compute sin by summing power series"""
    k = 0
    v = 0
    newterm = tol+1
    x = x % (2*pi)
    while abs(newterm)>tol and k<maxit:
        newterm = (-1)**k * x**(2*k+1) / factorial(2*k+1)
        v += newterm
        ## print(newterm,v)
        k += 1
    if (k==maxit):
        print("warning: reached max iterations")
    return(v)

def sin_series2(x,tol=1e-6,maxit=100):
    """Compute sin by summing power series: multiply"""
    k = 1
    v = 0
    x = x % (2*pi)
    newterm = x
    while abs(newterm)>tol and k<maxit:
        v += newterm
        newterm *= -1 * x**2 / ((2*k+1)*(2*k))
        ## print(newterm,v)
        k += 1
    if (k==maxit):
        print("warning: reached max iterations")
    return(v)


    
    
