import simplecrypt
f = open('passwords.txt', 'r')
g = open('encrypted.bin', 'rb')
pwd = []
b = g.read()
for line in f:
    try:
        print(simplecrypt.decrypt(line[:-1], b))
    except:
        continue
f.close()
g.close()



