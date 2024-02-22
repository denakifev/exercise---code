import time 
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

try:
    f = open('text.txt', 'r')
    while True: #Обычный способ читать файлы
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end =' ')
        time.sleep(4)
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла.')
finally:
    f.close()
    print('(Очистка: Закрытие файла)')