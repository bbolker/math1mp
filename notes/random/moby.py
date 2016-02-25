import urllib.request as ur
from io import TextIOWrapper
f = ur.urlopen("http://www.gutenberg.org/ebooks/2701.txt.utf-8")
f2 = TextIOWrapper(f)
val = f2.readline()
while not val[:15]=="Call me Ishmael":
    val = f2.readline()
all = val+f2.read()
words = all.lower().split()
w1 = words.count("whale")  ## 495
w2 = len(words)
print(w1)
print(w2)
print(w1/w2)
