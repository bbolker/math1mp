def roman_to_int(r):
    """convert roman to integer: step through string"""
    v = 0   ## initialize counter
    d = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
    ## iterate by index so we can check whether we are
    ##  on the last value or not
    for i in range(len(r)):
        val = d[r[i]]  ## dictionary lookup
        if i<(len(r)-1):  ## if not quite at end of string
            val_next = d[r[i+1]]
            if val_next > val:
                v -= val
            else:
                v += val
        else:
            v += val
    return(v)

assert(roman_to_int("XIX")==19)        
