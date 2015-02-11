def roman_to_int(r):
    """convert roman to integer: dictionary"""
    v = 0
    d = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
    for symbol in d:
        v += r.count(symbol)*d[symbol]
    return(v)

assert(roman_to_int("XVII")==17)
