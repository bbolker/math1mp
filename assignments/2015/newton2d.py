import numpy as np
import matplotlib.pyplot as plt

## Newton fractals in python  (1D)

def newtonstep(x,f,g):
    return(x-f(x)/g(x))

def newton(x0,f,g,tol=1e-8,maxstep=20):
    i=0
    x=x0
    while (i<maxstep and abs(f(x))>tol):
        x = newtonstep(x,f,g)
        i += 1
    return(x)

def f1(x):
    return(x**3-3)

def g1(x):
    return(3*x**2)

print(newton(-2,f1,g1))
print(newton(2,f1,g1))
print(newton(-2+0j,f1,g1))
print(newton(2+0j,f1,g1))
print(newtonstep(2+0j,f1,g1))

n = 101
x0vec = np.linspace(-5,5,n)+0.00001
res = np.zeros((n,n),dtype=complex)
## res[0] = newton(x0vec[0],f1,g1)
for i in range(n):
    print(i)
    for j in range(n):
        res[i,j] = newton(x0vec[i]+x0vec[j]*(0+1j),f1,g1)

plt.imshow(abs(res),interpolation="none")
plt.show()
## plt.plot(x0vec,res)
## plt.show()
