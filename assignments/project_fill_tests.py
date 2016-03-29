import numpy as np
## change this line to use your macid
from bolker_proj_fill import *  
print("all tests should result in True ...")
a = np.array([0,0,1,1,1,0,0,0,1,0,0,1,0])
print("test fillable (interior, r=default(1)):")
print(fillable(6,a))
print("test fillable (interior, r=1):")
print(fillable(6,a,1))
print("test not fillable (interior, r=1):")
print(not fillable(5,a,1))
print("test not fillable (interior, r=2):")
print(not fillable(6,a,2))
print("test fillable (edge,r=1)")
print(fillable(0,a))
print("test not fillable (edge,r=1)")
print(not fillable(12,a))
print("test not fillable (edge,r=2)")
print(not fillable(0,a,2))
print("test any_fillable (r=1)")
print(any_fillable(a))
b = a.copy()
b[[0,6,9]] = 1
print("test not any_fillable (r=1)")
print(not any_fillable(b))
print("test not any_fillable (r=2)")
print(not any_fillable(a,r=2))
b = a.copy()
print("strict test fill_one, seed=101")
## can't be absolutely sure that filling algorithm will use exactly
## 1 random number, so stream may not be identical?
np.random.seed(101)
fill_one(b)
c = a.copy()
c[6] = 1
print(all(b==c))
print("strict test fill_one: only one legal choice")
## there is only one legally fillable space (e[99]),
## so no matter what random number seed we use, that
## must be the one that gets filled ...
e = np.ones(100)
e[98:100] = 0
fill_one(e)
f = e.copy()
f[99] = 1
print(np.all(e==f))
print("loose test fill_one, seed=101")
print(np.sum(b)==np.sum(a)+1)
np.random.seed(101)
d = fill_sim(10)
print("loose test fill_sim(10), seed=101")
print(not any_fillable(d))
print("strict test fill_sim(10), seed=101")
print(all(d==np.array([0,1,0,0,1,0,1,0,0,1])))
np.random.seed(101)
print("loose test fill_sim(10), seed=101")
print(not any_fillable(d))
print("strict test fill_sim(6,2), seed=101")
np.random.seed(101)
e = fill_sim(6,2)
print(all(e==np.array([1,0,0,1,0,0])))
print("loose test fill_sim(6,2), seed=101")
print(not any_fillable(e,2))



