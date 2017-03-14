`def numint0(f,lo,hi,n):
    """brute-force numerical integration of a function"""
    dx = (hi-lo)/n
    x = np.arange(lo,hi,step=(hi-lo)/n)
    ## y = np.zeros(len(x))
    ## for i in range(len(x)):
    ##     y[i] = f(x[i])
    y = f(x)  ## vectorized function
    return(y.sum()*dx)

def numint1(f,lo,hi,tol,init_n=10):
    """adaptive integration routine"""
    prev = 1e9 # set to a ridiculous value
    n = init_n  # initial number of steps
    while True:  ## 'pythonic'
        cur = numint0(f,lo,hi,n)
        # print(n,prev,cur,abs(cur-prev))
        if abs(cur-prev)<tol: ## stopping condition
            break
        n *=2
        prev = cur
    return(cur)

def sqrtfun(x):
    return(np.sqrt(1-x**2))

print(numint1(sqrtfun,0.0,1.0,tol=1e-6))

##for n in [11,101,1001,10001,100001]:
##    print(n,numint0(sqrtfun,0.0,1.0,n)*4.0-np.pi)

