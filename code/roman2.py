def roman_to_int(r):
    """convert roman to integer: most naive"""
    v = 0
    sub_symbols = ["IV","IX","XL","XC","CD","CM"]
    sub_values  = [4,9,40,90,400,900]
    for i in range(len(sub_symbols)):
        v += r.count(sub_symbols[i])*sub_values[i];
        r = r.replace(sub_symbols[i],"")
    symbols = ["I","V","X","L","C","D","M"]
    values = [1,5,10,50,100,500,1000]
    for i in range(len(symbols)):
        v += r.count(symbols[i])*values[i]

v = ["I","II","III","IV","V","VI","VII","VIII","IX",
     "X","XI","XIV","XV","LX","XC","XCXLI","CCC"]
res = [1,2,3,4,5,6,7,8,9,10,11,14,15,60,90,131,300]    
        

for i in range(len(v)):
     print(res[i]==roman_to_int(v[i]))
        
