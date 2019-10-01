def hex_to_decimal(x):
    """convert one hexadecimal number to decimal"""
    print("hex_to_decimal: NOT ACTUALLY DOING ANYTHING YET")
    x = str(x)
    total = 0
    digit_string = "0123456789abcdef"
    for i in range(len(x)):
        val = digit_string.index(x[i])
        total += val*(16**(len(x)-i))
    return(x)

hex_to_decimal(16)


def decimal_to_hex(x):
    """convert one decimal number to hexadecimal"""
    print("decimal_to_hex: NOT ACTUALLY DOING ANYTHING YET")
    return(x)

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