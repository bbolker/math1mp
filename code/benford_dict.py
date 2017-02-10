def benford_dict(fn):
    """
    a function to read a file and count the
    distribution of first digits in the numbers.
    Assumes that each line has two words on it,
    and the second word is the number we're looking
    for.
    :param f: file name
    :return: list of length 10 with numbers of 0, 1, ... as first digit
    """
    # initialize
    f = open(fn)
    res = {}
    for L in f:
        # split up words in the line
        words = L.split(" ")
        # find the first character of the last word
        firstchar = words[-1][0]
        # increment the appropriate element of the return list
        if firstchar in res:
            res[firstchar] += 1
        else:
            res[firstchar] = 1
    return(res)

def benford_list(fnlist):
    """a function to read a list of files and
    return a list of lists of counts of first characters
    """
    res = []
    for fn in fnlist:
        res.append(benford_dict(fn))
    return(res)


if __name__=="__main__":
    print(benford_dict("benford_pop.txt"))
    mylist = ["benford_pop.txt","lakes3.txt"]
    print(benford_list(mylist))

