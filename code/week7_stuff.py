d = {"A":1,"B":2,"C":3}
print(d)
empty = {}  ## empty dictionary
print(d["A"])
print(d[1])
print(d["D"])
x = "D"
print(d[x])
x in d
d.keys()
x in d.keys() ## identical to x in d
d.values()
4 in d.keys()
3 in d.keys()
3 in d.values()

x = (("A",1),("B",2))
dict(x)
tuple(dict(x))

print(d)
d2 = {"F":5, "G":7, "H":10}
d.update(d2)
print(d)
print(d2)

dict(A=1,B=2,C=3)


d = dict(A=1,B=2,C=3)
for i in d:  ## loop over keys
    ## do something
    print(i)   
    
d.items()

print(d)
print(d2)

tt = (("a",1),("b",17))
print(dict(tt))
print(dict(tt).items())
print(tuple(dict(tt).items()))

## one-to-many dictionary inversion
def inv_dict(d):
    """ invert a dictionary d, allowing for multiple identical
    values for different keys; save new values as lists"""
    inv = {}  ## set up empty dictionary
    for k in d:
        new_key = d[k]
        new_value = k
        if d[k] in inv:
            inv[new_key] = inv[new_key] + [new_value]
        else:
            inv[new_key] = [new_value]
    return(inv)

d1 = {"A":1, "B":2, "C":2, "D":3}
print(inv_dict(d1))
d0 = {}
print(inv_dict(d0))
d2 = {"A":1, "B":[3,4,5], "C":2, "D":3}
inv_dict(d2)
d3 = {"A":1, "B":(3,4,5), "C":2, "D":3}
inv_dict(d3)

def get_grade_dict(fn):
    """retrieve student numbers and grades from a file
    (filename 'fn')
    """
    ## open file for reading
    f = open(fn, 'r')
    ## initialize empty dictionary
    result = {}
    ## go through the file one line at a time
    for line in f:
        words = line.strip().split()
        ## print(words)
        if words!=[]:  ## len(words)==0
            if words[0] in result:
                raise ValueError("repeated key:"+words[0])
            result[words[0]] = words[1]
    f.close()
    return(result)

d = get_grade_dict("grade_file.txt")
inv_dict(d)

def get_last_word(s):
    return(s.split()[-1])

def get_leading_digit(w):
    print(w)
    return(int(w[0]))

def ben_count(file_name):
   ## digits_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   digits_count = {}  ## empty
   f = open(file_name, 'r')
   for line in fn:
        print("line:",repr(line))
        last_word = get_last_word(line)
        print("last word:",repr(last_word))
        leading_digit = get_leading_digit(last_word)
        if leading_digit > 0:
            if not leading_digit in digits_count:
                ## I haven't seen this digit yet
                digits_count[leading_digit] = 1
            else:
                digits_count[leading_digit] += 1
   f.close()
   return digits_count

bdict = ben_count("benford_pop.txt")
