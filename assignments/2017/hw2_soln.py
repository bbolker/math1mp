def eratos(n):
    """eratosthenes' sieve
    """
    is_prime = (n+1)*[True]
    i = 2
    res = []
    while i<=n:
        res.append(i)
        j=2*i
        while j<=n:
            is_prime[j] = False
            j+=i
        i += 1
        while i<=n and not is_prime[i]:
            i+=1
    return(res)

def iterate(f,start,tol=1e-6,itmax=1000,print_it=False):
    """iteration program
    """
    it = 0
    y = start
    while abs(f(y)-y)>tol and it<itmax:
        if print_it:
            print(it,y,f(y),f(y)-y)
        y = f(y)
        it += 1
    return([it,f(y)])

def read_evens(fn):
    """count the number of even numbers in a text file
    """
    f = open(fn)
    c = 0
    for n in f:
        if int(n) % 2 == 0:
            c += 1
    return(c)
    
if __name__=="__main__":
    
    print(eratos(5))
    print(eratos(100))
    print(len(eratos(1000)))

##

    def testfun(x):
        return(1.5*x*(1-x))
    print(iterate(testfun,0.5))
    print(iterate(testfun,0.5,tol=1e-8))
    def testfun2(x):
        return(x/2)
    print(iterate(testfun2,1000)) 
    import math
    print(iterate(math.sqrt,1.01,tol=1e-4))
    print(iterate(math.cos,0))
    print(iterate(math.cos,0,tol=1e-8))
    print(iterate(math.cos,0,itmax=5))

    print(read_evens("even_nums.txt"))
