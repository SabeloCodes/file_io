# Open data.txt for reading
f = open('data.txt', 'r')

lines = f.read()
f.close()
print (lines)