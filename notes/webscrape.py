## http://stackoverflow.com/questions/12902783/where-is-beautifulsoup4-hiding
from bs4 import BeautifulSoup
import requests
import pandas as pd
from pytz import all_timezones
## http://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it
## http://stackoverflow.com/questions/10715965/add-one-row-in-a-pandas-dataframe

def get_web():
    r  = requests.get("http://www.cbsa-asfc.gc.ca/bwt-taf/menu-eng.html#_s1")
    data = r.text
    f = open("tempweb.html","w")
    f.write(data)
    f.close()
    return(None)

def get_df1(fn="tempweb.html"):
    f = open(fn)
    data = f.read()
    soup = BeautifulSoup(data)
    ## http://stackoverflow.com/questions/2010481/how-do-you-get-all-the-rows-from-a-particular-table-using-beautifulsoup
    tables = soup.findChildren('table')
    ## This will get the first (and only) table. Your page may have more.
    my_table = tables[0]
    ## You can find children with multiple tags by passing a list of strings
    rows = my_table.findChildren(['tr'])
    res = []
    for row in rows[2:]:  ## skip header lines
        cells = row.findChildren('td')    ## extract fields
        cc = cells[0].contents            ## first field is complex
        res.append([cc[0].get_text(),     ## office
                cc[2],                ## address
                cc[6].get_text(),     ## date-time
                cells[1].contents[0], ## commercial
                cells[2].contents[0]]) ## non-commercial
    c1 = pd.DataFrame(res) 
    c1.columns = [
        'office', 'address', 'datetime_text', 'commercial', 'noncommercial']
    ## c1.to_csv("tempdf.csv",index=False)
    return(c1)

## can't use attribute indexing to add a new column
def drop_last_word(x):
    ss = x.split(' ')
    return(' '.join(ss[:-1]))

def get_last_word(x):
    ss = x.split(' ')
    return(ss[-1])

def delay_transform(x):
    p = pd.Series([None]*len(x),dtype=float)
    for i in range(len(x)):
        if x[i]=="Not applicable":
            p[i] = None
        elif x[i]=="No delay":
            p[i] = 0
        elif "minutes" in x[i]:
            num = (x[i].split(' '))[0]
            p[i] = float(num)
        else:
            print(x[i])
    return(p)

## time zones, ugh ...
## http://wesmckinney.com/blog/easy-high-performance-time-zone-handling-in-pandas-0-8-0/


## http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python
import urllib.request
from xml.dom import minidom
## http://stackoverflow.com/questions/20439321/downloading-xml-file-with-python-3
def getXML(url= "http://apps.cbp.gov/bwt/bwt.xml"):
    uu = urllib.request.urlretrieve(url)
    mm = minidom.parse(uu[0])
    mm = mm.childNodes[0]  ## go down one level
    ## 0, 1, 2, 3 are updated date, time, number of ports
    res = []
    for n in mm.childNodes[3:]:
        line = []
        for p in n.childNodes:
            line.append(p.childNodes[0].data)
        res.append(p)
    return(res)

    

if __name__== "__main__":
    df = get_df1()
    dt_text = df.datetime_text.apply(drop_last_word)
    df['datetime'] = pd.to_datetime(dt_text)
    df['timezone'] = df.datetime_text.apply(get_last_word)
    df.noncommercial = delay_transform(df.noncommercial)
    df.commercial = delay_transform(df.commercial)
    print(df)


