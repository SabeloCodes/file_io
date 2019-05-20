
f = open('newfile.txt', 'a')
dataset = ['Hello','World','Welcome','To','File IO']
lines = '\n'.join(dataset)
f.writelines(lines)
f.close()