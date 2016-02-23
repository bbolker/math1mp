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

def compile_dict(d,L):
    """take a list and increment the dictionary accordingly,
    counting frequencies of all the first digits"""
    for i in L:
        update_dict(d,i)
    return(None)

if __name__ == "__main__":
   d = init_dict()
   update_dict(d,456)
   update_dict(d,237)
   print(d)
   print_dict(d)
   d = init_dict()
   compile_dict(d,[456,237])
   print_dict(d)
