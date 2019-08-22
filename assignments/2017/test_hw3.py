import numpy as np
import numpy.random as npr
from my_hw3 import *


print("Q1:")

a = np.array([[1,0],[1,0]])
npr.seed(101)
b = npr.randint(2,size=(8,8))
c = npr.rand(8,8)

print(all(calc_frac(a)==np.array([1.,0])))
print(all(calc_frac(a,1)==np.array([0.5,0.5])))
print(np.allclose(calc_frac(b),
  np.array([ 0.75 ,  0.5  ,  0.5  ,  0.125,  0.625,  0.75 ,  0.5  ,  0.75 ])))
print(np.allclose(calc_frac(b,axis=1),
  np.array([ 0.875,  0.625,  0.25 ,  0.75 ,  0.375,  0.75 ,  0.5  ,  0.375])))

print("Q2:")
try:
    calc_rel_frac(a)
    print(False)
except ValueError:
    print(True)

print(all(calc_rel_frac(a,1)==np.array([ 1.,  1.])))
print(np.allclose(calc_rel_frac(b),
                  np.array([ 6.,  4.,  4.,  1.,  5.,  6.,  4.,  6.])))
print(np.allclose(calc_rel_frac(b,axis=1),
   np.array([ 3.5,  2.5,  1. ,  3. ,  1.5,  3. ,  2. ,  1.5])))

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
print(np.asscalar(arg_cvmax(b)) is 3)
print(np.asscalar(arg_cvmax(b,1)) is 2)
print(np.asscalar(arg_cvmax(c)) is 7)
print(np.asscalar(arg_cvmax(c,1)) is 1)
print(np.asscalar(arg_cvmax(c,axis=1)) is 1)

