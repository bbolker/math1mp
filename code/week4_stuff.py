
x=2
x**2
round(1.204)
import math 
math.sin(2)
sin(2)
help("math")
math.inf > 1000000000000000000000000000000000000000000000

from math import sin, cos
sin(math.pi)

import numpy as np
np.array([1,2,3])

## user-defined modules
import sqr
sqr.sqr(4)
from sqr import *
sqr(5)
cube(5)

def repeat_fun(f,startval,n):
    """Given a function f and a starting value startval,
    apply the function n times (each time using the previous
    result as input)
    """
    y = startval
    for i in range(n):
        y=f(y)
    return(y)

def sqr(x):
    return(x*x)

def compose_fun(f,g,x):
    """compute the composition of two
    functions, f(g(x))"""
    x2 = g(x)
    result = f(x2)
    return(result)

	x = [[1,3],[4,5]]
2	y = [[2,6],[7,8]]
3	
4	def matmult(x,y):
5	    m = len(x[0]) ## number of columns of x
6	    n_rows_x = len(x)
7	    n_cols_y = len(y[0])
8	    result = []
9	    ## if m != len(y): 
10	       ## do something awful if number of col(x) != rows(y)
11	    for i in range(n_rows_x):
12	     result.append([])
13	     for j in range(n_cols_y):
14	        total = 0
15	        for k in range(m):
16	            print("i=",i,"j=",j,"k=",k,"xval",x[i][k],"yval",y[k][j])
17	            total += x[i][k] * y[k][j]
18	        print(total)
19	        result[i].append(total)
20	    return(result)
21	    
22	matmult(x,y)
23	matmult(x,x)


###
def has_dups(list1):
    return "False"

has_dups([1,2,3]) == False


def has_two(x):
    return(2 in x)

list1 = [1,2,3]
has_two(list1)
list1 = [1,2,3]
## run your code
has_dups = has_dups(list1)

##    return False