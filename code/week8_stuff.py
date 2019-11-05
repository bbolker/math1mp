s = "Hello"
s.lower()
s = "Hello, there is some punctuation!"
"hello there is some punctuation"

import string
print(string.punctuation)

def clean_string(s):
    result = ""
    for i in s:
        if not i in string.punctuation:
            result += i
    result = result.lower()
    return result

clean_string(s)

def make_dict(text):
    d = {}
    for word in text:
        if not word in d:
            d[word] = 1
        else:
            d[word] = d[word]+1
    return(d)

def make_dict2(text):
    d = {}
    for i in range(len(text)-1):
        word = text[i]
        next_word = text[i+1]
        if not word in d:
            d[word] = [next_word]
        else:
            d[word].append(next_word)
    return(d)

## create a dictionary that counts the number of times that
## each word occurs

def make_word_count(filename="mobydick.txt"):
    ## open and read file
    ## split it into words
    ## get rid of the punctuation etc.
    ## go through and count the words
    f = open(filename, "r")
    text = f.read()
    text = clean_string(text)
    text = text.split()
    d = make_dict2(text)
    return(d)

m = make_word_count()

print(m[1000:1010])
print(len(m))
print(m.count("receive"))
print(m.count("whale"))
print(m.count("Whale"))
print(m.count("whale,"))

d = make_word_count()
d["whale"]
d["because"]
d["whale"]
print(len(d))

## next time

import random as rnd
for i in range(100):
    print(rnd.randrange(5))
L = ["a","d","c"]
L[rnd.randrange(len(L))]
rnd.choice(L)
d = {"a":1, "b":2, "q":16}
rnd.choice(tuple(d.keys()))
rnd.sample(d.keys(),3)

def get_random_string(n):
    s = ""
    for i in range(n):
        s += rnd.choice("abcdefghijkl")
    return(s)

rnd.seed(101)
get_random_string(100)
rnd.seed(101)
get_random_string(100)

##

def generate_markov(m,n=20):
    ## pick a word at random from the keys
    ## for i in range(n):
    ##    add the current word to results
    ##    pick a new word from the values
    ##      associated with the current word
    result = ""
    word = rnd.sample(m.keys(),1)[0]
    for i in range(n):
        result = result + " " + word
        word = rnd.sample(m[word],1)[0]
    return(result)

print(generate_markov(m))

##
import numpy
import numpy as np ## abbreviation ...

x = [1,4,5,8]
a0 = np.array(x)
print(a0)
print(x)
a = np.array(x, dtype=float)
print(a)
print(repr(a))

np.array(tuple(x))
np.array(range(5))
np.arange(5)
np.arange(1,12,2)
np.zeros(10)
np.ones(10)
np.zeros((10,2))
np.zeros((3,5,4))

x = np.arange(28).reshape((7,4))
print(x)
x[0,3]
x[1:3,-1]
x[1:3,-1:]
x[:,-1]
for i in range(x.shape[1]):
    print(x[:,i].sum())
    
    
x.sum(axis=0)
print(x)
x.reshape(28)
x.reshape(x.shape[0]*x.shape[1])
x.flatten()
np.array(x.shape).prod()
x.sum()
x.mean()

x.fill(16)
x

a = np.arange(9).reshape((3,3))
b = np.arange(10,19).reshape((3,3))

a + b
np.concatenate((a,b))

##
import random
def gamblers_ruin(start=10,max=50):
    ## iterate until you get to zero or max
    ## return tuple: (0 = lost, 1 = won,
    ##   [number of steps]
    i = 0
    x = start
    while x>0 and x<max:
        x += random.sample([-1,1],1)[0]
        i += 1
    if x==0:
        result = 0 ## lost
    else:
        result = 1
    return(np.array((result, i)))

gamblers_ruin()

sim = np.zeros((1000,2))
for i in range(1000):
    sim[i,:] = gamblers_ruin()
    
sim[:,0].mean()  ## prob of winning
sim[:,1].max()   ## max number of steps
sim[:,1].min()   ## min number of steps
