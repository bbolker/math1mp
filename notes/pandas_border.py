import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## border info at
## http://www.math.mcmaster.ca/bolker/misc/borderinfo.dat
p = pd.read_csv("borderinfo.dat",sep=" ",skiprows=1,header=None)
p.columns = ["row","locs","statustime","delay","lanes","type","date","time"]
p.index = pd.to_datetime(p.date+" "+p.time)
p = p.drop(["date","time"],axis=1)
print(p.shape)

pbuf = p[(p.locs.str.contains("Buff")) & (p.type=="regular")]
pbuf_hour = pbuf.delay.groupby(pbuf.index.hour)
pbuf_meandelay = pbuf_hour.aggregate(np.mean)
pbuf_maxdelay = pbuf_hour.aggregate(np.max)

pbuf_meandelay.plot()
## select buffalo/niagara crossings
## figure out day-of-week
## aggregate and calculate values
## by season?

