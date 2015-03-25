import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
v = "MEASLES_Cases_1909-2001_20150322001618.csv"
p  = pd.read_csv(v,skiprows=2,na_values=["-"])  ## read in data
p.index = p["YEAR"]+(p["WEEK"]-1)/52
pp = p.drop(["YEAR","WEEK"],axis=1)             ## drop year/week columns
plt.figure(figsize=(5,5))
pp.plot(legend=False,logy=True)                 ## plot (on log scale)
plt.savefig("pix/measles1.png")
ptot = pp.sum(axis=1)
plt.figure(figsize=(5,5))
ptot.plot(logy=True)
plt.savefig("pix/meastot.png")
ptotweek = ptot.groupby(p.WEEK)
ptotweek.plot()
plt.savefig("pix/measwk.png")
