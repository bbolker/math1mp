if False:
    print("no")
if True:
    print("yes")
    print("something else")
    
print("yes")
print("something else")

x=2
if (x<=0):
    print("what??")
elif(x==1):
    print("one")
elif(x==2):
    print("two")
else:
    print("many")
    
## solution to CodingBat "date fashion" Q.
def date_fashion(you, date):
  if you <=2 or date <= 2:
    result = 0
  elif you >= 8 or date >=8:
    result = 2
  else:
    result = 1
  return(result)

import math
math.log2(20)

help("math")

## initialization
n =0
x = 16
while x>1:
    x = x/2
    n = n+1
print(n)

## infinite loops below: watch out!
if False:
   while True:
      print("hello")
   x = 0
   while True:
      x= x+1
      print(x)
        
## sum values of x^i from i=0 to i=17
x = 5  ## initialize x
sum = 0
for i in range(0,2000):
    sum = sum + x**i
print(sum)

## warm up for 'coin counting problem'
toonies = total // 2
total = total - 2*toonies

## code fra
d = 2
coins = total // d
total = total - d*coins


total = 5.73
res = []   # empty list
denoms = [2,1,0.25,0.1,0.05]
for d in denoms:
    ## FIXME: make results into integers?
    ## FIXME: round nickels appropriately
    coins = total // d
    total = total - d*coins
    res.extend(coins)
    ## res.extend([coins])
    ## res.append(coins)
    print(d,total,coins)
print(res)

