
from johaln4_proj_wipeaway import *
#from my_project import *
import numpy as np
import numpy.random as npr

## tests for wipeaway project
if "run_sim" in locals().keys():
    print("running tests for wipeaway project")
    npr.seed(101)
    print("run_sim, p=0:",run_sim(N=10,D=1,p=0)==10)
    print("testing p=1: this should only take a few seconds ... otherwise you probably have an infinite loop")
    try:
        run_sim(N=10,D=1,p=1)
        print("run_sim, >itmax",False)
    except RuntimeError:
        print("run_sim, >itmax",True)
    a = np.zeros(500)
    for i in range(500):
        a[i]=run_sim(N=5,D=2)
    m = a.mean()
    print("run_sim,N=5,D=2:",m>15 and m<18)
    nsim = 1000
    print("exp_val 1:",np.isclose(exp_val(np.arange(5)),3.0))
    if not "collect_sims" in locals().keys():
        print("collect_sims not implemented yet")
    else:
        c = collect_sims(nsim,5,2,0.5)
        print("collect_sims 1:",len(c)==10000)
        print("collect_sims 2:",c.sum()==nsim)
        e = exp_val(c)
        print("collect_sims 3:",e>15 and e<18)
        if not "many_sims" in locals().keys():
            print("many_sims not implemented yet")
        else:
            m = many_sims((2,10),(1,1),p=0,nsim=10)
            print(m)
            correct = np.arange(2,11).reshape((9,1))
            print(correct)
            print("many_sims 1:",np.allclose(m,correct))

## tests for cipher project
if "read_cipherdef" in locals().keys():
    print("running tests for cipher project")
    t1 = "hello"
    t2 = "goodbye"
    t3 = "squeamish ossifrage"
    ##
    d0 = read_cipherdef("dict0.txt") ## trivial dictionary
    d1 = read_cipherdef("dict1.txt")
    ##
    if not "sub_cipher" in locals().keys():
        print("sub_cipher not implemented")
    else:
        print("basic 1",sub_cipher(t1,d1)=="ncooy")
        print("basic 2",sub_cipher(t2,d1)=="myyaivc")
        ##
        def roundtrip(msg,d):
            """round-trip test for substitution cipher"""
            trans = sub_cipher(msg,d)
            orig = sub_cipher(trans,reverse_dict(d))
            return(orig == msg)
        ##
        print("roundtrip 1",roundtrip("hello",d1))
        print("roundtrip 2",roundtrip("goodbye",d1))
        print("roundtrip 3",roundtrip("hello goodbye",d1))
        if not "min_crib_dist" in locals().keys():
            print("min_crib_dist not implemented")
        else:
            print("min_crib 1",min_crib_dist(t1,t1)==0)
            print("min_crib 2",min_crib_dist(t1,"aello")==1)
            print("min_crib 3",min_crib_dist(t1,"hellx")==1)
            print("min_crib 4",min_crib_dist(t1,"defgh"+t1)==0)
            t1T = open("test1T.txt").read().strip()
            
            print("min_crib 5",min_crib_dist(t3,sub_cipher(t1T,reverse_dict(d1)))==0)
            print("min crib 6",min_crib_dist(t3,sub_cipher(t1T,d1))==16)
            print("min crib 7",min_crib_dist(t3,sub_cipher(t1T,d0))==16)
	
