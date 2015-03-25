import integrate

def convolve(f1,f2,r,a,b,n):
    def f12(x):
        return(f1(x)*f2(x-r))
    r = integrate.int2(f12,a,b,n)
    return(r)

def cfun(f1,f2,a,b,n):
    def c(r):
        def f12(x):
            return(f1(x)*f2(x-r))
        return(integrate.int2(f12,a,b,n))
    return(c)

def unif(x):
    if 0<x<1:
        return(1)
    else:
        return(0)

print(convolve(unif,unif,0.5,-3,3,1000))
cc = cfun(unif,unif,-3,3,1000)
print(cc(0.5))
cc2 = cfun(unif,cc,-3,3,1000)
print(cc2(0.25))
cc3 = cfun(unif,cc,-3,3,1000)
print(cc3(0.5))
