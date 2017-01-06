from sympy import sieve
import matplotlib.pyplot as plt


def primewalk(n=100,draw_plot=True):
    """ Compute and draw 'prime walk' plot for primes <n
        http://tinyurl.com/primewalk
    """
    ## get magic list of primes
    primes = list(sieve.primerange(1,n))
    ## initialize; set starting point and direction
    ## (horizontal, to the right)
    x = [0]
    y = [0]
    direction = "right"
    for i in range(1,len(primes)):
        pdiff = primes[i]-primes[i-1]
        if direction=="right":
            x.append(x[i-1]+pdiff)
            y.append(y[i-1])
            direction="down"
        elif direction=="down":
            x.append(x[i-1])
            y.append(y[i-1]-pdiff)
            direction="left"
        elif direction=="left":
            x.append(x[i-1]-pdiff)
            y.append(y[i-1])
            direction="up"
        elif direction=="up":
            x.append(x[i-1])
            y.append(y[i-1]+pdiff)
            direction="right"
    if (draw_plot):
        fig, ax = plt.subplots()
        ax.plot(x,y)
        plt.show()
    return(None)

if __name__=="__main__":
    primewalk(100)
