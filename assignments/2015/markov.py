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
        new_word = r.choice(ngram_dict[last_words])
    else:
        ngram_list = list(ngram_dict.keys())
        new_word = ngram_list[r.randint(len(ngram_list))][0]
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
    r.seed(101)
    gg = generate_markov_step([""],dd)

    for i in range(50):
        generate_markov_step(cur_list,dd)
## print(cur_list)    

## dd2 = make_ngram_dict("darwin_origins.txt")
## cur_list = ["which"]
## for i in range(50):
##    generate_markov_step(cur_list,dd)
## print(cur_list)

