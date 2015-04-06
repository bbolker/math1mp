import numpy.random as npr
from project_answers import *

## YAHTZEE

## test that choice() and randint() give same results
npr.seed(1001)
sides=6
p1 = tuple(npr.choice(range(1,sides+1),size=5))
npr.seed(1001)
p2 = tuple(npr.randint(1,sides+1,size=5))
assert(p1==p2)

L = (6,2,6,4,5)  ## outcome when we use npr.randint()
L2 = (1,4,4,6,6)
L3 = (6,1,5,6,6)
L4 = (6,6,5,6,6)

def eq_list_or_tuple(x,y1,y2=None):
    firstmatch = sorted(tuple(x))==sorted(tuple(y1))
    if y2==None:
        return(firstmatch)
    else:
        return(firstmatch or sorted(tuple(x))==sorted(tuple(y2)))

npr.seed(1001)
assert(eq_list_or_tuple(single_roll(5),L))

assert(eq_list_or_tuple(new_roll(L),L2))
## add some more specific tests for correct behavior with ties,
## differently ordered rolls, etc.
assert(eq_list_or_tuple(new_roll((1,1,2,6,6)),L3))
npr.seed(1001)
assert(eq_list_or_tuple(sim_yahtzee(1,5),L))
assert(eq_list_or_tuple(sim_yahtzee(3,5),L4))

assert(est_yahtzee_prob(1)==0)

## testing for approximately uniform values across rolls
z = [0]*6
for i in range(1000):
    for j in single_roll(5):
        z[j-1] += 1
assert(z==[842, 857, 800, 846, 848, 807])

npr.seed(1007)
est1 = est_yahtzee_prob(100000)
assert(abs(est1-0.046)<0.001)

## http://www.datagenetics.com/blog/january42012/ uses Markov matrix multiplication to get 4.6029%
## if this is correct the standard deviation is
## sqrt((p*(1-p))/n) == 0.0006626
## +/- 2 SD is 0.0013 so with n=100,000
## we should get answers between about 0.0447 and 0.0474

## http://statistics.about.com/od/ProbHelpandTutorials/a/What-Is-The-Probability-Of-Rolling-A-Yahtzee.htm  says 3.43%; but doesn't take account of switching
## best numbers

## MARKOV

test1 = "adf, xyz. LMNO"
cs = clean_string(test1)
assert(cs=="adf xyz lmno")
## split_string not mentioned in web page
## ss = split_string(cs)
## assert(ss==['adf', 'xyz', 'lmno'])
d = add_ngrams(cs.split(' '),2,dict())
assert(d==dict([(('xyz',),['lmno']),(('adf',),['xyz'])]))

testfn = "darwin.txt"
dd = make_ngram_dict(testfn)
cur_list = ["which"]
npr.seed(101)
gg = generate_markov_step([""],dd)
for i in range(10):
    generate_markov_step(cur_list,dd)
assert(cur_list==['which', 'we', 'are', 'being', 'growth', 'with', 'its', 'several', 'powers', 'having', 'been'])


