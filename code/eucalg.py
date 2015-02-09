def euc_alg_loop(a,b):
    '''modular Euclid algorithm by looping'''
    while b>0:
       r = a % b
       a = b
       b = r
        ## print(a,b)
    return(a)

def euc_alg_rec(a,b):
    '''modular Euclid algorithm by recursion'''
    if (b==0):
        return(a)
    m = min(a,b)
    return(euc_alg_rec(m,max(a,b) % m))

assert(euc_alg_loop(36,42)==6)
assert(euc_alg_loop(407,361)==1)
assert(euc_alg_rec(407,361)==1)
