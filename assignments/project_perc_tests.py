import numpy.random as npr
from bolker_proj_perc import *
npr.seed(101)
a = rand_bin_array(5,0.5)
print("rand_bin_array, seed=101, strict")
print(np.all(a==np.array([[1,1,0,0,1],[1,0,1,1,0],
                       [1,0,0,1,1],[0,0,1,1,0],
                       [1,1,0,0,0]])))
print("rand_bin_array, seed=101, loose")
npr.seed(101)
a2 = rand_bin_array(1000,0.5)
ac = np.sum(a2)
print(ac>470 & ac<530)
print("check_path, bottom row, empty")
print(not check_path(4,2,a))
print("check_path, bottom row, full")
print(check_path(4,1,a))
print("check_path, next-to-last row, full")
print(check_path(3,2,a))
print("check_path, third row, full")
print(check_path(2,3,a))
print("check_path, third row, empty")
print(not check_path(2,0,a))
print("check_path, next-to-last row, empty")
print(not check_path(3,3,a))
print("check_path, second row, full")
print(check_path(1,2,a))
print("check_path, second row, empty")
print(not check_path(1,0,a))
print("check_path, first row, empty")
print(not check_path(0,0,a))
print("check_path, first row, full")
print(check_path(0,1,a))
print("perc_path, OK")
print(perc_path(a))
b = a.copy()
b[2,[3,4]]=0
print("perc_path, not OK")
print(not perc_path(b))



# [[1 1 0 0 1]
#  [1 0 1 1 0]
#  [1 0 0 1 1]
#  [0 0 1 1 0]
#  [1 1 0 0 0]]


