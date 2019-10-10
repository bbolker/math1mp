def hex_to_decimal(x):
    """convert one hexadecimal number to decimal"""
    x = str(x)
    total = 0
    digit_string = "0123456789abcdef"
    for i in range(len(x)):
        val = digit_string.index(x[i])
        total += val*(16**(len(x)-i-1))
    return(total)

hex_to_decimal(16)
hex_to_decimal("deadbeef")

def decimal_to_hex(x):
    """convert one decimal number to hexadecimal"""
    digit_string = "0123456789abcdef"
    i = 0
    result = ""
    while True:
        next_n = (x // 16**i) % 16
        next_digit = digit_string[next_n]
        result = next_digit + result
        i = i+1
        if x < 16**i:
            break
    return(result)

def decimal_to_hex_2(x):
    """convert one decimal number to hexadecimal"""
    digit_string = "0123456789abcdef"
    i = 0
    result = ""
    while True:
        next_n = (x // 16**i) % 16
        next_digit = digit_string[next_n]
        result = next_digit + result
        i = i+1
        h = hex_to_decimal(result)
        if str(h)==str(x):
            break
    return(result)

def decimal_to_hex_3(x,base=16):
    """convert one decimal number to hexadecimal"""
    digit_string = "0123456789abcdefghijklmnopqrstuvwyz"
    result = ""
    while x>0:
        next_n = x % base
        next_digit = digit_string[next_n]
        result = next_digit + result
        x = x - next_n
        x = x // base
    return(result)

        

decimal_to_hex(257)
decimal_to_hex_2(257)

def hex_convert():
    """input two hexadecimal numbers,
    convert to base 10,
    print them,
    add them,
    convert the sum back to hexadecimal,
    print the result
    """
    print("enter x:")
    x = input()
    ## should we check that x is legal (i.e
    ## only contains 0-9 and a-f ?)
    print("enter y:")
    y = input()
    ## don't do this! too early
    ## x = int(x)  ## convert to integer
    ## y = int(y)
    x = hex_to_decimal(x)
    y = hex_to_decimal(y)
    print(x)
    print(y)
    z = x + y
    z = decimal_to_hex(z)
    print(z)
    return(None)


## playing with indexing
hex_convert()
digit_string = "0123456789abcdef"
x = "c"
digit_string.index(x)

## alternative
i = 0
while i<len(digit_string) and x!=digit_string[i]:
    i = i +1