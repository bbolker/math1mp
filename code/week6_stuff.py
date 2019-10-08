f = open("test.txt")
type(f)
print(f)
print(f.closed)
f.close()
print(f.closed)

f = open('test.txt', 'r')
contents = f.read()
print(contents)
print(repr(contents))
f.close()

contents[6]
contents[5]
