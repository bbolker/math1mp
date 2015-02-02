def roman_to_int(r):
    """convert roman to integer: step through string"""
    v = 0
    symbols = ["I","V","X","L","C","D","M"]
    values = [1,5,10,50,100,500,1000]
    ## iterate by index so we can check whether we are
    ##  on the last value or not
    for i in range(len(r)):
        spos = symbols.index(r[i])
        if i<(len(r)-1):
            spos_next = symbols.index(r[i+1])
            if values[spos_next]>values[spos]:
                v -= values[spos]
            else:
                v += values[spos]
        else:
            v += values[spos]
    return(v)

        
