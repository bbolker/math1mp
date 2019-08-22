
h=3
q=0
for h in range(1,h+1):
    print("#1:",h)
    h=h*h
    q=q+h
    print("#2:",h,q) 

## version 2
h=3
q=0
for h in range(1,h+1):
    q=q+h*h
    print(h,q) 
