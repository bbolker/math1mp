# mandelbrot.py
# Modified from
# https://batchloaf.wordpress.com/2013/02/10/creating-julia-set-images-in-python/
import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

r = numpy.zeros((251,201))  # set up a matrix of zeros
nmax=255
for i in range(0,250):
    for j in range(0,200):
        c = complex(i/100-2,j/100-1)
        z = 0
        n = 0
        while abs(z) < 2 and n <= nmax:
            z = z*z + c
            n = n+1
        r[i,j] = n/nmax  ## note: Py3
plt.imshow(r) # set up graph
plt.show()    # display graph


