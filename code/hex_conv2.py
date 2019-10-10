def decimal_to_hex(x):
    value_str = "0123456789abcdef"
    i = 0
    res = ""
    while x>0:
        n = x % 16  ## find next digit
        x -= n      ## subtract digit (what's left is div by 16)
        x = x // 16 
        res = value_str[n] + res ## add digit to *front* of result
    return res

import timeit
## https://writeonly.wordpress.com/2008/09/12/using-python-timeit-to-time-functions/
timeit.timeit("decimal_to_hex(100000000)",
              "from __main__ import decimal_to_hex",
              number=10000)
