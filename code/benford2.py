import io

def setup_dict():
    """set up dictionary"""
    dd = dict(zip(range(10),(0,)*10))
    return(dd)

## equivalent for letters:
## dict(zip(list(string.ascii_lowercase),(0,)*26))

def update_dict(dd,n,digit=0):
    """add specified digit of number n to dictionary dd"""
    dd[int(n[digit])] += 1
    return(None)

def benford_dist(str_list,
                 digit=-2):
    dd = setup_dict()
    for s in str_list:
        update_dict(dd,s,digit=digit)
    return(dd)

## easier way to convert file to list?
def get_list(fn):
    f = io.open(fn)
    in_list = []
    for i in f:
        in_list.append(i.strip())
    return(in_list)

    ## equivalently:
def get_list2(fn):
    f = io.open(fn)
    r = f.read()
    in_list = r.split("\n")
    return(in_list[:-1])
    
print(benford_dist(get_list2("lakes3.txt"),digit=-1))

## Benford's law applies to data that are not dimensionless, so the numerical values of the data depend on the units.
