# julia.py - Generate a Julia Set image
# Written by Ted Burke, modified BMB
# https://batchloaf.wordpress.com/2013/02/10/creating-julia-set-images-in-python/
# Last updated 10-2-2012/30-12-2014
import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

r = numpy.zeros((401,401))
c = complex(0,0.65)
for i in range(0,400):
    for j in range(0,400):
        z = complex(i/100-2,j/100-2)
        n = 0
        nmax=20
        while abs(z) < 10 and n <= nmax:
            z = z*z + c
            n = n+1
        r[i,j] = n/nmax  ## note: Py3
plt.imshow(r)
plt.show()





