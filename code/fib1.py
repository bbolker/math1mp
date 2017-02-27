def fib1(n=10):
    """compute fibonacci numbers"""
    res = [1,1]
    for i in range(n):
        res.append(res[-1] + res[-2])
    return(res)

def fib_recurse(n=10):
    """compute fibonacci numbers recursively"""
    if n<=2:
        return(1)
    return(fib_recurse(n-1)+fib_recurse(n-2))

print(fib1())
print(fib_recurse())