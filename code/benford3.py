import urllib.request as ur
import csv
import io
import re

def init_dict():
    """initialize dictionary of counts"""
    d = dict()
    for i in range(1,10):
        d[str(i)]=0
    return(d)

def update_dict(d,n):
    """given a number n, increment the counter in dictionary d
    that corresponds to its first digit"""
    s = str(n)
    d[s[0]] += 1
    return(None)

def print_dict(d):
    """print a dictionary in sorted order"""
    for i in sorted(d.keys()):
        print(i+'='+str(d[i]))
    return(None)

def compile_dict(L):
    d = init_dict()
    """take a list and create a corresponding dictionary,
    counting frequencies of all the first digits"""
    for i in L:
        update_dict(d,i)
    return(d)

def get_last_words(fn):
    """retrieve a list of the last words of each line of a file"""
    f = open(fn)
    res = []
    for L in f:
        wordlist = L.split()
        lastword = wordlist[-1]
        res.append(lastword)
    return(res)

def is_num(cc):
    return(bool(re.search("^[0-9.]+$",cc)))

def is_num2(cc):
    try:
        float(cc)
        return(True)
    except ValueError:
        return(False)

def get_words_from_url_csv(url,pos=3):
    f = ur.urlopen(url)
    cr = csv.reader(io.TextIOWrapper(f))
    res = []
    for L in cr:
        if is_num(L[0]):
            break
    res.append(L[pos])
    for L in cr:
        if not is_num(L[0]):
            break
        else:
            if L[pos] != "(X)":
                res.append(L[pos])
    return(res)
        
if __name__ == "__main__":
   d = init_dict()
   update_dict(d,456)
   update_dict(d,237)
   d = compile_dict([456,237])
   print_dict(d)
   stars_list = get_last_words("stars.txt")
   d = compile_dict(stars_list)
   print_dict(d)
   pop_list = get_words_from_url_csv("http://www.census.gov/popest/data/cities/totals/2011/tables/SUB-EST2011-01.csv")
   d = compile_dict(pop_list)
   print_dict(d)
   
