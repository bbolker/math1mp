def roman_to_int(r):
    """convert roman to integer: most naive"""
    v = 0
    v += r.count("XC")*90
    r = r.replace("XC","")
    if "IX" in r:
        r = r.replace("IX","")
        v += 9
    if "XL" in r:
        r = r.replace("XL","")
        v += 40
    if "IV" in r:
        r = r.replace("IV","")
        v += 4
    while "C" in r:
        r = r.replace("C","",1)
        v += 100
    while "L" in r:
        r = r.replace("C","",1)
        v += 50
    while "X" in r:
        r = r.replace("X","",1)
        v += 10
    while "V" in r:
        r = r.replace("V","",1)
        v += 5
    while "I" in r:
        r = r.replace("I","",1)
        v += 1
    return(v)

## can continue ...

v = ["I","II","III","IV","V","VI","VII","VIII","IX",
     "X","XI","XIV","XV","LX","XC","XCXLI","CCC"]
res = [1,2,3,4,5,6,7,8,9,10,11,14,15,60,90,131,300]    
        

for i in range(len(v)):
     print(res[i]==roman_to_int(v[i]))
        
