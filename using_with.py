poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''
f = open('text.txt', 'w')
f.write(poem)
f.close()
print('поэма записана в файл')
with open('text.txt', 'r') as f:
    for line in f:
        print(line, end = ' ')
