# https://adesquared.wordpress.com/2013/06/16/using-python-beautifulsoup-to-scrape-a-wikipedia-table/
from bs4 import BeautifulSoup
import urllib
# wiki = "http://en.wikipedia.org/wiki/List_of_postcode_districts_in_the_United_Kingdom"
country_pop_wiki = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

def get_vals(url,label_col=1,val_col=2,ncells=6):
    page = urllib.request.urlopen(wiki)
    soup = BeautifulSoup(page,"lxml")
    table = soup.find("table", { "class" : "wikitable sortable" })
    labels = []
    vals = []
    for row in table.findAll("tr"):
        cells = row.findAll("td")
            if len(cells) == ncells:
                labels.append(cells[label_col].find(text=True))
                vals.append(cells[val_col].find(text=True))

def write_vals(labels,vals,fn="benford_pop.txt"):
    f = open(fn,"w")
    for i in range(len(labels)):
        cc = labels[i].replace(" ","_")
        f.write(cc+" "+vals[i]+"\n")


# something wrong with some lines: Nagorno-Karabakh Republic, etc.

