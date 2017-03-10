import numpy as np
import numpy.random as npr
from my_hw3 import *


print("Q1:")

a = np.array([[1,0],[1,0]])
npr.seed(101)
b = npr.uniform(size=(3,3))

print(all(calc_frac(a)==np.array([1.,0])))
print(all(calc_frac(a,1)==np.array([0.5,0.5])))
print(np.allclose(calc_frac(b),
                  np.array([ 0.33162883,  0.71651922,  0.52797165])))
print(np.allclose(calc_frac(b,axis=1),
                  np.array([ 0.37184681,  0.56356517,  0.64070772])))

print("Q2:")
try:
    calc_rel_frac(a)
    print(False)
except ValueError:
    print(True)

print(all(calc_rel_frac(a,1)==np.array([ 1.,  1.])))
print(np.allclose(calc_rel_frac(b),
                  np.array([ 1.        ,  2.1606059 ,  1.59205592])))
print(np.allclose(calc_rel_frac(b),
                  np.array([ 1.        ,  2.1606059 ,  1.59205592])))

print("Q3:")
e = np.eye(4)
f = np.diag([1],k=3)
g = e[1:,:]

print(check_symmetric(e))
print(not check_symmetric(e+f))
print(check_symmetric(e+f*1e-9))
print(not check_symmetric(e+f*1e-9,1e-10))
try:
    check_symmetric(g)
    print(False)
except ValueError:
    print(True)

print("Q4:")
print(np.asscalar(arg_cvmax(b)) is 2)
print(np.asscalar(arg_cvmax(b,1)) is 0)
print(np.asscalar(arg_cvmax(b,axis=1)) is 0)

