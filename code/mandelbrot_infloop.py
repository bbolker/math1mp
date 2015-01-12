# mandelbrot.py

import numpy

r = numpy.zeros((251,201))  # set up a matrix of zeros
nmax=255
for i in range(0,251):
    for j in range(0,201):
        c = complex(i/100-2,j/100-1)
        z = 0
        n = 0
        while abs(z) < 2 and n <= nmax:
            z = z*z + c
        r[i,j] = n


