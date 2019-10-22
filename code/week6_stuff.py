f = open("test.txt")
type(f)
print(f)
print(f.closed)
f.close()
print(f.closed)

f=open("doesnt_exist.txt")
import os
os.getcwd()
os.listdir()


f = open('test.txt', 'r')
contents = f.read()
print(contents)
print(repr(contents))
contents2 = 'abc\ndef\n123\n'
contents3 = 'abc/ndef/n123/n'
print(contents3)
contents == contents2
contents3 == contents
f.close()
start = f.read(4)
print(start)
contents[6]
nextchars = f.read(3)
print(nextchars)
print(repr(nextchars))
f.read()
f.read()
f.read(1000)
f.close()

f = open('test.txt')
lines = f.readlines()
print(repr(lines))

f = open("test.txt")
for line in f:
    print(line)
    line_u = line.upper()
    print(line_u)
f.close()   

f = open("test.txt")
L = f.readline()
print(L)
print(repr(L))
L[:-1]
print(repr(L[:-1]))
if (L[-1]=='\n'):
    L = L[:-1]
L.strip()
test = "   abc    \n"
test.strip()  ## get rid of spaces and newlines

test = "hello goodbye whatever"
test.split(" ")
test.split(",")
test.strip().split(" ") ## method chaining
test2 = test.strip()
test3 = test2.split(" ")

os.getcwd()
os.chdir("/home")
os.listdir()
os.chdir("/home/jupyter")
os.getcwd()

f = open("test.txt")
line = next(f) ## read one line
print(line)
line = next(f)
##42,"John Smith","carpenter"


f = open("test.txt")
finished = False
while not finished:
   try:
      print("trying next line")
      line = next(f)
      print(line)
   except StopIteration:
      print("hit a StopIteration error")
      finished = True
    
def benford_count(fn):
    """fn is the file name"""
    f = open(fn)
    count = [0,0,0,0,0,0,0,0,0,0]
    ## go through the file one line at a time
    ## for each line:
    ##    split the line into words
    ##    get the second word
    ##    get the first character of the second word
    ##    convert to an integer
    ##    increment the appropriate counter
    for line in f:
        print(line)
        words = line.split(" ")
        number = int(words[1][0])
        counts[number] = counts[number]+1
    f.close()
    return(tuple(count))

benford_count("benford_pop.txt")
