def fizzbuzz(n):
    res = [] ## create an empty list
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            res.append("fizzbuzz")
        elif i%3==0:
            res.append("fizz")
        elif i%5==0:
            res.append("buzz")
        else:
            res.append(str(i))
    return(res)