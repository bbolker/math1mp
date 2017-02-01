def gridsearch(g,xl,xh,n=1000):
    """
    a function to find the root of another function
    :param g: a function
    :param xl: low value
    :param xh: high value
    :param n: number of steps between xl and xh to try
    :return: root value
    """
    delta = (xh-xl)/n
    x = [xl]   # x values
    gx = [g(xl)]  # g(x) values
    for i in range(n):
        x.append(x[-1]+delta)
        gx.append(g(x[-1]))
    ## second pass: now go through these lists and
    ##  find the minimum absolute value
    minval = abs(gx[0])
    minx = x[0]
    for i in range(n+1):
        if abs(gx[i])<minval:
            minval = gx[i]
            minx = x[i]
    return([minx,minval])

if __name__=="__main__":
    import math
    print(gridsearch(math.cos,0,math.pi/2,n=3))
    def testfun(x):
        return(math.cos(x)-x)
    print(gridsearch(testfun,0,math.pi/2))