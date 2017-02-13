import os

def markov_dict(fn="darwin_nopunct.txt"):
    """read a file and convert it to a Markov dictionary"""
    f = open(fn)
    s = f.read() # read the whole file into a single string
    d = {} # initialize empty dict
    s = s.replace("\n"," ") # replace newlines with spaces
    w = s.split(" ") # break into a list of words
    print(len(w)) # number of words
    # loop over the indices of the list:
    #  stop one before the end because we want
    #  to access the *next* word as well
    for i in range(len(w)-1):
        if not w[i] in d: # word to add
            d[w[i]] = [] # initialize with empty list
        d[w[i]].append(w[i+1]) # add next word
    return(d)

import random
def markov_create(d,n=20):
    """generate a random string based on a dictionary"""
    # random choice from keys as starting point
    res = [random.choice(list(d.keys()))]
    for i in range(n):
        # random choice from following words
        nextword = random.choice(d[res[i]])
        res.append(nextword)
    sentence = " ".join(res) # squash into a string
    return(sentence)

if __name__=="__main__":
    m = markov_dict("mobydick.txt")
    # find longest sequence
    maxlen = 0
    for i in m:
        curlen = len(m[i])
        if curlen>maxlen:
           longest = (curlen,i,m[i])
           maxlen = curlen
    print(longest)
    # print random sequence
    print(markov_create(m))
