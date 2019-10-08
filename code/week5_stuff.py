t = (17, "q", 4, 6)
a, b, c, d = t
print(a)
print(d)

x = 1
y = 2
## swap these values - y = 1, x = 2
anything_i_want = y
y = x
x = anything_i_want


x, y = y, x

x = [1,2,3]
y = tuple(x)

def f(x):
    print(x**2)
    
def g(x):
    return(x**2)

a = f(2)
b = g(2)

f(2)
g(2)

####
## grid search
import math
def testfun0(x):
    return(x-23)

def testfun(x):
    return(math.exp(x)-x-1.5)

def grid(f,endpts,n=1001):
    """
    f: a Python function that takes one float argument and returns one float value
    endpts: a 2-element tuple of the end points
    n: number of intervals to evaluate
    """
    ## figure out what points to try 
    a, b = endpts ## or a = endpts[0]; b = endpts[1]
    fxmin = math.inf  ## minimum value of abs(f(x)) achieved so far
    xmin = 0        ## Position at which f(x) was achieved
    for i in range(n+1):
        x = a + i*(b-a)/n
        fx = abs(f(x))
        if fx<fxmin:
            ## found a better value: save the y and the x location
            fxmin = fx
            xmin = x
    return((xmin,fxmin))
        
grid(testfun0,(0,50))
grid(testfun0,(22.95,23.05))
grid(testfun0,(22.999,23.001))

grid(testfun0,(0,50), n = 100000001)
grid(testfun0,(22.999,23.001))

## TO DO:
## check if the root is actually bracketed or not?
##   i.e. test if f(a)*f(b)<0
## ? return both the xmin and the fxmin value
##