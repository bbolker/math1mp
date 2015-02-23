import urllib.request as ur
import csv
from io import TextIOWrapper
import re  ## for first_num()

def setup_dict():
    """set up dictionary"""
    dd = dict(zip(range(10),(0,)*10))
    return(dd)


## http://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
def remove_all(x,v=","):
    """remove all instances of v from x"""
    x = x.replace(v,"")
    return(x)


def update_dict(dd,n,digit=0):
    """add specified digit of number n to dictionary dd"""
    n = remove_all(n)
    dd[int(n[digit])] += 1
    return(None)

def first_num(cc):
    return(bool(re.search("^[0-9]+$",cc[0])))
           
# def get_str(x):
#     """get a string from a bytes object"""
#     y = str(x)[2:]
#     return(y)

    
# def get_num(x,n,sep=","):
#     """extract a number from a separated line; remove quotes"""
#     w = x.split(sep)
#     r = remove.all(w[n],"\"")
#     return(r)

## http://stackoverflow.com/questions/16243023/how-to-resolve-iterator-should-return-strings-not-bytes
## http://stackoverflow.com/questions/2647723/urllib2-to-string

def benford_dist(url="http://www.census.gov/popest/data/cities/totals/2011/tables/SUB-EST2011-01.csv",
                 pos=3,
                 digit=-2):
    f = ur.urlopen(url)
    cr = csv.reader(TextIOWrapper(f))
    dd = setup_dict()
    cc = next(cr)  ## initialize with first line; Python3-specific
                   ## = cr.next() in Python2
    while not first_num(cc):  ## skip header
        cc = next(cr)
    while first_num(cc):      ## go until we don't see numbers any more
        update_dict(dd,cc[pos],digit=digit)
        cc = next(cr)
    return(dd)

print(benford_dist())

## Benford's law applies to data that are not dimensionless, so the numerical values of the data depend on the units.
