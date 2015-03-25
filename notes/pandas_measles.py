import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

v = "MEASLES_Cases_1909-2001_20150322001618.csv"
p  = pd.read_csv(v,skiprows=2,na_values=["-"])  ## read in data
p = p[p.YEAR>1935]  ## dump trash
## set up fancier date-index
yearstr = p.YEAR.apply(format)
weekstr = p.WEEK.apply(format,args=["02"])
datestr = yearstr+"-"+weekstr+"-0"
dateindex = pd.to_datetime(datestr,format="%Y-%U-%w")
p.index = dateindex
##  p.index = p.YEAR+(p.WEEK-1)/52
pp = p.drop(["YEAR","WEEK"],axis=1)             ## drop year/week columns
ptot = pp.sum(axis=1)
ptotweek = ptot.groupby(p.WEEK)
ptotweekmean = ptotweek.aggregate(np.mean)
per=pd.cut(p.YEAR,bins=[1935,1965,1978,2002])
ptotweekper = ptot.groupby((per,p.WEEK))
ptotweekpermean = ptotweekper.aggregate(np.mean)
## ptotweekpermean = ptotweekpermean.reset_index()

## log-scale plot of totals
if False:
    plt.figure(figsize=(5,5))
    pp.plot(legend=False,logy=True)                 ## plot (on log scale)
    plt.savefig("pix/measles1.png")
    plt.close()

if True:    
    plt.figure(figsize=(5,5))
    ptot.plot(logy=True)
    plt.savefig("pix/meastot.png")
    plt.close()

if True:
    plt.figure(figsize=(5,5))
    ptotweekmean.plot()
    plt.savefig("pix/measwk.png")
    plt.close()

if True:
    plt.figure(figsize=(5,5))
    for i in range(3):
        tmp = ptotweekpermean.iloc[(i*52):(i+1)*52-1]
        tmp /= tmp.max()
        tmp.index = np.arange(len(tmp))
        tmp.plot()
    plt.savefig("pix/measwkper.png")
    plt.close()
