from sympy import sieve
primes = sieve.primerange(1,1000)
x = [0]
y = [0]
axis = "x"
direction = 1
for i in range(1,1000):
    pdiff = primes[i]-primes[i-1]
    if axis=="x":
        x.append(x+direction*pdiff)
        y.append(y[i-1])
        axis=="y"
    else:
        direction=-1*direction
        y.append(y+direction*pdiff)
        x.append(x[i-1])
        axis=="x"

    
