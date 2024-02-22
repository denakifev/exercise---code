import random


print('**********Добро пожаловать в числовую угадайку**********')
n = int(input('Выберете границу загаданного числа '))
a = random.randint(1,n)
def is_valid(s):
    return s.isdigit() and 1<=int(s)<= n

flag = True
count = 1
while flag:
    b = input('Введите число ')
    if is_valid(b):
        b = int(b)
    else:
        print('Может введем число правильно?')
        continue
    if b<a:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count+=1
    elif b>a:
        count+=1
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'Поздравляю, вы угадали за {count} попыток')
        print('Вы хотите сыграть ешё?(да/нет)')
        if input().strip().lower() == 'да':
            n = int(input('Выберете границу загаданного числа '))
            a = random.randint(1,n)
            count = 1
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            flag = False
         