chars = ("M","D","C","L","X","V","I")
vals = (1000,500,100,50,10,5,1)

import numpy as np

def roman_to_integer(input):
    """translate a sequence of characters from a roman numeral
    into an integer"""
    v = 0
    for i in range(len(chars)):
        v += vals[i]*input.count(chars[i])
    return(v)

def roman_to_integer2(input):
    """translate a sequence of characters from a roman numeral
    into an integer"""
    v = np.zeros(len(chars))
    for i in range(len(chars)):
        v[i] = input.count(chars[i])
    return((np.array(vals)*v).sum())

def roman_to_integer3(input):
    """ allow for subtraction rule"""
    v = 0
    c = 0 ## counter for the denomination: position in vals
    i = 0
    while i<len(input):
        while input[i]==chars[c]: ## another of the current value
            v += vals[c]
            i += 1
            if i==len(input):
                break
        ## do something about subtraction
        if c+2<len(chars) and input[i] in input[i]==chars[c+2]:
            print("subtraction")
            v -= vals[c+2]
            i += 1  ## skip to next character
        c += 1  ## step to the next denomination
    return(v)

print(roman_to_integer3("MDCXI"))



def integer_to_roman(input):
    """as it says, translate integer to roman"""
    ##input % vals[i]