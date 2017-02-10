def bisection(g,xl,xh,prec=1e-6):
    """search for a root by bisection
    """
    gh = g(xh)
    gl = g(xl)
    decr_fun = (gl>gh)
    xm = (xl+xh)/2
    gm = g(xm)
    while abs(gm)>prec:
        if (gm>0 and decr_fun) or (gm<0 and not decr_fun):
            xl = xm # move lower boundary up to middle
        else:
            xh = xm # move upper boundary down to middle
        xm = (xl+xh)/2
        gm = g(xm)
    return([xm,gm])

if __name__=="__main__":
    # def testfun(x):
    #     return(2-x)
    # print(bisection(testfun,0,5,1e-20))
    def testfun2(x):
        return(x-2)
    print(bisection(testfun2,0,5,1e-20))

