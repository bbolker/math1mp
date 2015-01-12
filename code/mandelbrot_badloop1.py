# mandelbrot.py

import numpy

r = numpy.zeros((251,201))  # set up a matrix of zeros
nmax=255
for i in range(0,251):
    for j in range(0,201):
        c = complex(i/100-2,j/100-1)
        n = 0
        while abs(z) < 2 and n <= nmax:
            z = 0
            z = z*z + c
            n += 1
        r[i,j] = n
