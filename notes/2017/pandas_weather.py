import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## http://climate.weather.gc.ca/climateData/hourlydata_e.html?timeframe=1&Prov=ON&StationID=49908&hlyRange=2011-12-14|2015-03-23&Year=2015&Month=3&Day=23

def url_string(station=49908,year=2014,month=2):
    return("http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID="+format(station)+"&Year="+format(year)+"&Month="+format(month)+"&timeframe=1&submit=Download+Data")

## p = pd.read_csv(url_string(),skiprows=15,encoding="latin1",index_col="Date/Time",parse_dates=True)
p = pd.read_csv("eng2.csv",skiprows=14,encoding="latin1",index_col="Date/Time",parse_dates=True)
p.columns = [
    'Year', 'Month', 'Day', 'Time', 'Data Quality', 'Temp (C)', 
    'Temp Flag', 'Dew Point Temp (C)', 'Dew Point Temp Flag', 
    'Rel Hum (%)', 'Rel Hum Flag', 'Wind Dir (10s deg)', 'Wind Dir Flag', 
    'Wind Spd (km/h)', 'Wind Spd Flag', 'Visibility (km)', 'Visibility Flag',
    'Stn Press (kPa)', 'Stn Press Flag', 'Hmdx', 'Hmdx Flag', 'Wind Chill', 
    'Wind Chill Flag', 'Weather']
p = p.dropna(axis=1,how='all')
p["Temp (C)"].plot()
plt.savefig("pix/weather1.png")
p = p.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
plt.close()

temp = p[['Temp (C)']]
temp["Hour"] = temp.index.hour

temphr = temp.groupby('Hour')
medtmp = temphr.aggregate(np.median)
maxtmp = temphr.aggregate(np.max)
mintmp = temphr.aggregate(np.min)
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1)
ax.plot(medtmp,label="median")
ax.plot(mintmp,label="min")
ax.plot(maxtmp,label="max")
ax.legend()
fig.savefig("pix/medtmp.png")
