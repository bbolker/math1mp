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
    bad_number = 0
    ## count = []
    ## for i in range(100):
    ##    count.append(0)
    counts = [0]*10 ## [0,0,0,0,0,0,0,0,0,0]
    ## go through the file one line at a time
    ## for each line:
    ##    split the line into words
    ##    get the second word
    ##    get the first character of the second word
    ##    convert to an integer
    ##    increment the appropriate counter
    for line in f:
        print(line)
        words = line.split(" ") ## list of words
        try:
            last_word = words[-1]
            first_letter = last_word[0]
            number = int(first_letter)
            ##number = int(words[1][0])
        except ValueError:
            bad_number += 1
        ##    print("bad number")
        counts[number] = counts[number]+1
    f.close()
    s = sum(counts)
    for i in range(len(counts)-1):
     ## counts[i] /= s
        counts[i] = counts[i]/counts[i+1]
    if bad_number>0:
        print(bad_number,"bad number(s)")
    return(tuple(counts[1:-1]))

benford_count("benford_pop.txt")

vowels = {'a', 'e', 'i', 'o', 'u'}
print(type(vowels))
print(vowels)
vowels2 = {'u','a', 'e', 'i', 'o', 'u', 'e', 'a'}
print(vowels2)
vowels == vowels2
print({1, 2, 3, 'a'} == {'a', 1, 1, 3, 2, 'a'})
print(set('hello world!'))

'a' in vowels


small = {0, 1, 2, 3}
mid = {3, 4, 5, 6, 7}
big = {7, 8, 9}
big.add(10)
small.remove(0)
print(small, big)
print(small.intersection(mid))
print(small.union(big))

word_char = "1a2b"
bad_word = "ghij"
hex_chars = "0123456789abcdef"
set(word_char) <=  set(hex_chars)
set(bad_word) <=  set(hex_chars)
