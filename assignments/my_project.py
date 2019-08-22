import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

def run_sim(N=20,D=6,p=0.5,itmax=5000):
    """run wipeaway simulation"""
    c = N
    it = 0
    while (c!=0):
        d = npr.random_integers(1,D)*npr.choice((-1,1),p=(1-p,p))
        if (c+d>=0 and c+d<=N):
            c=c+d
        it += 1
        if it>itmax:
            raise RuntimeError
    return(it)

def collect_sims(nsim,N,D,p=0.5,nmax=10000):
    """count numbers of sims at each number of rolls"""
    a = np.zeros(nmax)
    for i in range(nsim):
        a[run_sim(N,D,p)] += 1
    return(a)

def exp_val(a):
    """return expected value of a vector indexed from 0"""
    return(np.sum(np.arange(len(a))*a/a.sum()))

def many_sims(N_vals,D_vals,p=0.5,nsim=100):
    """run many simulations, return array of expected values"""
    res = np.zeros((N_vals[1]-N_vals[0]+1,D_vals[1]-D_vals[0]+1))
    N_vec = np.arange(N_vals[0],N_vals[1]+1)
    D_vec = np.arange(D_vals[0],D_vals[1]+1)
    for i in range(len(N_vec)):
        for j in range(len(D_vec)):
            res[i,j] = exp_val(collect_sims(nsim,N_vec[i],D_vec[j],p))
    return(res)

## http://stackoverflow.com/questions/11481644/how-do-i-assign-multiple-labels-at-once-in-matplotlib
def plot_results(N_vals,D_vals,a,fn="tmp.png"):
    """plot results"""
    fig, ax = plt.subplots()
    for i in range(len(D_vals)):
        ax.plot(N_vals,a[:,i],label="D="+str(D_vals[i]))
    ax.set_ylabel("expected number of rolls")
    ax.set_xlabel("starting value (N)")
    ax.legend(loc="upper left")
    plt.savefig(fn)

####


import numpy as np
from numpy.random import choice, shuffle
from string import ascii_lowercase

def sub_cipher(msg,d):
    """docstring here"""
    res = ""
    d[" "] = " "  ## leave spaces intact
    for i in msg:
        res += d[i]
    return(res)

def reverse_dict(d):
    """another docstring"""
    d2 = {}
    for i in d:
        d2[d[i]] = i
    return(d2)

def read_cipherdef(fn):
    """docstring here"""
    f = open(fn)
    r = f.readlines()
    s0 = r[0].strip()
    s1 = r[1].strip()
    d = {}
    for i in range(len(s0)):
        d[s0[i]]=s1[i]
    return(d)

def min_crib_dist(crib,msg):
    n = len(crib)
    m = len(crib) ## max value
    for i in range(len(msg)-n+1):
        c = 0
        for j in range(n):
            if crib[j]!=msg[i+j]:
                c+=1
        if (c<m):
            m = c
    return(m)

def rand_dict(keys=ascii_lowercase):
    """another docstring"""
    v = np.array(list(keys))
    shuffle(v)
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = v[i]
    return(d)

def dict_swap(d,n=1):
     swap1 = choice(np.array(list(d.keys())),n,replace=False)
     swap2 = choice(swap1,n,replace=False)
     shuffle(swap2)
     d2 = d.copy()
     for i in range(n):
         d2[swap1[i]] = swap2[i]
     return(d2)

    
    
if __name__ == "__main__":

    import os
    if not "manysims.npy" in os.listdir():
        a = many_sims((10,25),(3,8),nsim=1000)
        np.save("manysims.npy",a)
    else:
        a = np.load("manysims.npy")
    N_vals = np.arange(10,26)
    D_vals = np.arange(3,9)
    plot_results(N_vals,D_vals,a,"manysims.png")

##
    ndict = 10000
    npr.seed(101)
    cipher_res = np.zeros(ndict)
    t1T = open("test1T.txt").read().strip()
    if not "cipher_hist.npy" in os.listdir():
        for i in range(ndict):
            cipher_res[i] = min_crib_dist("squeamish ossifrage",sub_cipher(t1T,rand_dict()))
        np.save("cipher_hist.npy",cipher_res)
    else:
        cipher_res = np.load("cipher_hist.npy")
    fig, ax = plt.subplots()
    plt.hist(cipher_res)
    ax.set_xlabel("Minimum Hamming distance")
    ax.set_ylabel("Number of simulations")
    plt.savefig("cipher_hist.png")
