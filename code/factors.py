## from math import sqrt,floor

def find_factors(a):
    """find integer factors (other than 1 and a) by brute force"""
    factors = []
    i = 2
    maxfac = a ## floor(sqrt(a))+1
    while i<=maxfac:
        ## print(i,a%i,a//i,factors)
        if a%i==0:
            factors += [i]
            a = a // i
        else:
            i += 1
    return(factors)

def merge_factors(f1,f2):
    '''merge common factors'''
    res = []
    for i in f1:
        if i in f2:
            f2.remove(i)
            res += [i]
    return(res)

def common_factors(f1,f2):
    '''find common factors'''
    m = merge_factors(find_factors(f1),find_factors(f2))
    return(m)
    
assert(find_factors(36)==[2,2,3,3])
assert(find_factors(42)==[2,3,7])
assert(common_factors(36,42)==[2,3])
assert(common_factors(407,361)==[])
