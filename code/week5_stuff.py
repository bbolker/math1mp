t = (17, "q", 4, 6)
a, b, c, d = t
print(a)
print(d)

x = 1
y = 2
## swap these values - y = 1, x = 2
anything_i_want = y
y = x
x = anything_i_want


x, y = y, x

x = [1,2,3]
y = tuple(x)

def f(x):
    print(x**2)
    
def g(x):
    return(x**2)

a = f(2)
b = g(2)

f(2)
g(2)
