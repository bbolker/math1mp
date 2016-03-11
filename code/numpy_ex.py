### miscellaneous numpy examples
import numpy as np

## compute mean of natural numbers up to 7
a = np.arange(1,8)
b = a**2      ## square each value (elementwise)
c = b.mean()  ## or np.mean(b)
print(c)

## set up an array containing repeated rows (0, 0.2, 0.4, 0.6, 0.8)
x = np.arange(0,1,0.2)      ## set up one row
z = (x,x,x,x,x)             ## make five copies, by brute force
y = np.reshape(z,(5,5))     ## reshape

## an alternative approach -- make a one-element
## tuple containing the array. Duplicate it 5 times (giving a
## *tuple of 1D arrays*) and then convert it to a vector
np.array((x,)*5)

## yet another approach
np.concatenate((x,x,x,x,x))

## another way ... 
(np.arange(0,5,0.2) % 1).reshape((5,5))

## multiply two different arrays ...
a = np.arange(21).reshape(3,7)
b = a.reshape(7,3)  ## or np.arange(21).reshape(7,3)
np.dot(a,b)

## take a matrix and center/scale the columns to
##  have mean zero and std 1
a = np.arange(9).reshape((3,3))
m = np.mean(a,axis=0)
s = np.std(a,axis=0)
a2 = (a-m)/s

## sort an array by the third column
a = np.array([[1,2,3],[4,5,0],[2,1,9]])
a[a[:,2].argsort()]
