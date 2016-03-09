import numpy as np
import matplotlib.pyplot as plt

def logist_map(r,nt=100,x0=0.5):
   """ run the logistic map """
   x = np.zeros(nt)
   x[0] = x0
   for t in range(1,nt):
      x[t] = r*x[t-1]*(1-x[t-1])
   return(x)

def logist_map2(x0,r,t_trans,t_save):
     """version that only saves values after a transient"""
     res = np.zeros(t_save)
     x = x0
     for i in range(t_trans):
         x = r*x*(1-x)
     for i in range(t_save):
         res[i] = x
         x = r*x*(1-x)
     return(res)
