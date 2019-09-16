import urllib
import re
from datetime import date

## http://mypiday.com/
## http://mypiday.com/results/?date=19-9-10&ck=f26ffb24
## easier in Mathematica/Wolfram language:
##  https://blog.wolfram.com/2015/03/12/pi-or-pie-celebrating-pi-day-of-the-centuryand-how-to-get-your-very-own-piece-of-pi/
pi_url = "http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html"
pi_stuff = str(urllib.request.urlopen(pi_url).read())
pi_stuff2 = re.sub("\\\\n","",pi_stuff)          ## remove newlines
p = re.search("3.1415[0-9]+",pi_stuff2).group(0) ## find digits of pi

p.find("19910")  ## 8356, agrees with Wolfram
p.find("2019910") ## -1: not found

def make_pi(n=1000):
   q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
   for j in range(n):
      if 4 * q + r - t < m * t:
         yield m
         q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
      else:
         q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


def make_pi_string(n=1000):
    pi_str = ""
    for i in make_pi(int(n)):
        pi_str += str(i)
    return(pi_str)

import timeit

timeit.timeit('make_pi_string(1e4)',number=1)

x= make_pi_string(1e5)

## https://www.craig-wood.com/nick/articles/pi-chudnovsky/
        


    

