def lincong(start=5,n=10,a=2,c=3,m=10):
    """linear congruential generator"""
    x = [start]
    for i in range(n):
       newx = (a*x[-1]+c) % m
       x.append(newx)
    return(x)

for i in range(10):
    print(lincong(start=i))