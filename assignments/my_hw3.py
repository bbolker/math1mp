import numpy as np
def calc_frac(a,axis=0):
    return(a.mean(axis=axis))

def calc_rel_frac(a,axis=0):
    c = calc_frac(a,axis)
    if any(c==0):
        raise ValueError
    return(c/c.min())

def check_symmetric(a,tol=1e-8):
    s = a.shape
    if s[0] != s[1]:
        raise ValueError
    return(np.allclose(a,a.transpose(),rtol=0,atol=tol))

def arg_cvmax(a,axis=0):
    cv = a.std(axis=axis)/a.mean(axis=axis)
    return(cv.argmax())

