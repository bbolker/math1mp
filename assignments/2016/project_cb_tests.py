import numpy as np
from numpy.random import seed

## change this line to use your macid
from bolker_proj_cbinom import *
seed(101)
r1 = np.array([rbinom(10,0.5) for i in range(20)])
print("test rbinom (strict test, seed=101)")
print(all(r1==[4, 5, 3, 3, 6, 6, 6, 3, 5, 4, 7, 3, 6, 6, 3, 4, 3, 3, 6, 5]))
seed(101)
r2 = np.array([rbinom(10,0.5) for i in range(10000)])
print("test rbinom (loose test, seed=101)")
x2 = np.sum(r2==5)
print(x2>2300 & x2<2600)  ## should be correct 99.9% of the time ...
print("test cb_gen (strict test, seed=101)")
seed(101)
print(cb_gen(20,1,0.2)==(15,5))
print("test cb_gen (loose test, seed=101)")
seed(101)
r3 = [cb_gen(20,1,0.2) for i in range(10000)]
r3c = r3.count((15,5))
print(r3c>1600 & r3c<1800)
seed(101)
print("test cb_sim (strict test, seed=101)")
r4 = cb_sim(20,1,0.2)
print(r4==(1,5,9,5,1))
seed(101)
print("test cb_sim (loose test, seed=101)")
r5 = [cb_sim(20,1,0.2) for i in range(10000)]
r5c = r5.count((1,5,9,5,1))
print(r5c>75 & r5c<85)
print("update_cb_dict (basic)")
d={}
update_cb_dict(d,(1,2,1))
print(d=={(1, 2, 1): 1})



