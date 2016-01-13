import numpy.random as npr

def single_roll(n,fixed=(),sides=6):
    """roll a total of n sides-sided dice once;
    add fixed to the total
    """
    newroll = tuple(npr.choice(range(1,sides+1),size=n-len(fixed)))
    ## newroll = tuple(npr.randint(1,sides+1,size=n-len(fixed)))
    return(newroll+fixed)

def new_roll(vals,sides=6):
    maxval = 0
    maxnum = 0
    ## find max val
    ## should we worry about undefined behaviour if there
    ## are equal numbers of two types, e.g. (1,1,3,3,5) ?
    for i in range(1,sides+1):
        v = vals.count(i)
        if v>=maxnum:
            maxnum=v
            maxval=i
    fixed = (maxval,)*maxnum
    if (maxnum==len(vals)):
        return(vals)
    s = single_roll(len(vals),fixed=fixed,sides=sides)
    return(s)

def is_yahtzee(vals):
    return(vals.count(vals[0])==len(vals))
    
def sim_yahtzee(nrolls,dice,sides=6,return_success=False):
    """simulate a specified number of dice rolls of n dice
       Return a boolean True/False value depending on whether
       you achieve all dice the same
    """
    values = single_roll(dice,(),sides)
    if return_success and is_yahtzee(values):
        return(True)
    if (nrolls>1):
        for i in (1,range(nrolls)):
            values=new_roll(values,sides)
            if return_success and is_yahtzee(values):
                return(True)
    return(values)

def est_yahtzee_prob(nsims,nrolls=3,dice=5,sides=6):
    """estimate the probabilities of Yahtzee for a specified number
       of rolls, dice, and sides"""
    n_yahtzee = 0
    for i in range(nsims):
        s = sim_yahtzee(nrolls,dice,sides)
        if s.count(s[0])==dice:
            n_yahtzee += 1
    return(n_yahtzee/nsims)


## http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
def choose_index(probs):
    cmf = probs[0]
    choice = npr.random()
    for k in range(len(probs)):  ## was xrange but moved to python3
        if choice <= cmf:
            return k
        else:
            cmf += probs[k+1]
            
## start to work on analytic/recursive calculation:
##
## assume n of a kind rolled on previous roll;
## either n>2 matching previous >1
## or count number matching previous val
def prob_n_of_n(nrolls,dice,sides=6):
    for i in range(nrolls):
        probs = [prob_n_of_a_kind(i,sides)]
    return(None)

def prob_n_of_a_kind(n,sides=6):
    """probability of rolling n of a kind of a particular value:
    """
    (1-(sides-1/sides)**n)
    return(None)

    import numpy.random as r

def clean_string(str):
    """remove all punctuation from a string"""
    dropList = [",",".",";","-","*","/"]
    str = str.lower()
    for i in dropList:
        str = str.replace(i,"")
        str = str.replace("\n"," ")
    return(str)

def split_string(str):
    """split a string on spaces into a list of words"""
    return(str.split(" "))

def add_ngrams(strList,n=2,cur_dict=dict()):
    """add all n-grams from a string to the current dictionary"""
    for i in range(len(strList)-n+1):
        tt = tuple(strList[i:i+n-1])
        if tt in cur_dict:
            cur_dict[tt] += [strList[i+n-1]]
        else:
            cur_dict[tt] = [strList[i+n-1]]
    return(cur_dict)

def make_ngram_dict(fn,n=2):
    """make an n-gram dictionary from a file"""
    f = open(fn)
    cur_dict = dict()
    whole_list = []
    for line in f:
        cs = split_string(clean_string(line))
        whole_list += cs
    cur_dict = add_ngrams(whole_list,n,cur_dict)
    return(cur_dict)
    
def generate_markov_step(cur_list,ngram_dict,n=2):
    """pick a markov step from a dictionary"""
    last_words =  tuple(cur_list[-(n-1):])
    if last_words in ngram_dict:
        new_word = npr.choice(ngram_dict[last_words])
    else:
        ngram_list = list(ngram_dict.keys())
        new_word = ngram_list[npr.randint(len(ngram_list))][0]
    cur_list.append(new_word)
    return(new_word)

if __name__ == "__main__":
    test1 = "adf, xyz. lmno"
    cs = clean_string(test1)
    ss = split_string(cs)
    d = add_ngrams(ss,2,dict())
    testfn = "../../math1mp/misc/darwin.txt"
    dd = make_ngram_dict(testfn)
    cur_list = ["which"]
    npr.seed(101)
    gg = generate_markov_step([""],dd)

    for i in range(50):
        generate_markov_step(cur_list,dd)
## print(cur_list)    

## dd2 = make_ngram_dict("darwin_origins.txt")
## cur_list = ["which"]
## for i in range(50):
##    generate_markov_step(cur_list,dd)
## print(cur_list)


     
     


