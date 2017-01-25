def make_change(total,denoms=[2,1,0.25,0.1,0.05],debug=False,round_value=False):
    ## round to lowest denomination
    m = round(1/denoms[-1])
    total = round(total*m)/m
    res = [0]*len(denoms)
    for i in range(len(denoms)):
        d = denoms[i]
        cur = total // d
        total -= d*cur
        if (round_value):
            total = round(total,2)
        if (debug):
            print(i,cur,total)
        res[i] = cur
    return(res)
    
if __name__=="__main__":
    print(make_change(5.73))
    print(make_change(3.16,debug=True))
    print(make_change(3.16,debug=True,round_value=True))
