## https://stackoverflow.com/questions/50260574/wget-content-disposition-using-python
## https://drive.google.com/drive/folders/1WJCDEU34c60IfOnG4rv5EPZ4IhhW9vZH
## https://stackoverflow.com/questions/39263929/how-can-i-read-tar-gz-file-using-pandas-read-csv-with-gzip-compression-option
## get weather data for Hamilton
import urllib.request
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## day is always ignored
## month is ignored if getting daily data (tf=2); gets whole year
def get_weather(stationID, year, month=1, tf = 2):
    print(stationID, year)
    url = f"http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID={stationID}&Year={year}&Month={month}&Day=14&timeframe={tf}&submit=Download+Data"
    if os.path.exists("tmp.csv"):
        os.remove("tmp.csv")
    urllib.request.urlretrieve (url, "tmp.csv")
    x = pd.read_csv("tmp.csv",index_col="Date/Time",parse_dates=True)
    return x

res = []
for year in range(1870,1959):
    res.append(get_weather(4931, year=year))
r = pd.concat(res).dropna(axis=1,how='all')
len(res)    

r.to_csv("hamilton_weather1.tar.gz", compression="gzip")
r2 = pd.read_csv("hamilton_weather1.tar.gz", compression="gzip",
              index_col="Date/Time",parse_dates=True)

res = []
for year in range(1959,2012):
    res.append(get_weather(4932, year=year))
r = pd.concat(res).dropna(axis=1,how='all')
r.to_csv("hamilton_weather2.tar.gz", compression="gzip")


res = []
for year in range(2012,2019):
    res.append(get_weather(49908, year=year))
r = pd.concat(res).dropna(axis=1,how='all')
r.to_csv("hamilton_weather3.tar.gz", compression="gzip")

len(res)

allres = []
for i in range(1,4):
    allres.append(
        pd.read_csv(f"hamilton_weather{i}.tar.gz", compression="gzip",
                    index_col="Date/Time",parse_dates=True)
    )
r = pd.concat(allres)

fig, ax = plt.subplots()
ax.plot(r["Total Snow (cm)"])
fig.savefig("tmp.png")

ax.plot(r["Mean Temp (°C)"])
fig.savefig("tmp2.png")


                  
