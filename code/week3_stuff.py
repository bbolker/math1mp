## function practice

x = 5
if x<2:
    print("small")
elif x < 5:
    print("medium")
else:
    print("big")
    
    
def categorize(x):
    if x<2:
        result = "small"
    elif x < 5:
        result = "medium"
    else:
        result = "big"
    return(result)

def categorize(x):
    if x<2:
        return("small")
    elif x < 5:
        return("medium")
    else:
        return("big")
    
def categorize(x):
    if x<2:
        return("small")
    if x < 5:
        return("medium")
    return("big")


c = categorize(5)
print(c)
categorize(3.5)
categorize(1)

def add_element(my_list,new_thing):
    my_list.append(new_thing)

x = [1,2,"q"]
y = add_element(x,"b")

def my_fun(x,a=0,b=0,c=0,d=0,e=0,f=0,g=0):
    ## silly function ...
    return(x+a+b+c+d+e+f+g)

my_fun(1)
my_fun(x=1,g=1,a=2)
my_fun(g=1,a=2,x=1)

import math
math.log(2.71828)
math.log(2.71828,10)

def two_plus_three():
    return(2 plus 3)
    ## return(2+3)
    
## errors

L = ["a", "b", "c","d"]
L[3]

L[3:]
result = []
for i in range(len(L)-1):
    result.append(L[i:(i+2)])
print(result)
