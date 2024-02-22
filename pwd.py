import random
import time

digits =  '0123456789'
lowercase_letters= 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
special_symbols = 'il1Lo0O'

print('**********Привет, я сгенерирую для тебя сколько угодно паролей**********')
time.sleep(2.0)
print('Итак, начнем')
n  = int(input('Введите количество паролей '))
time.sleep(1.0)
list_of_pwd = []
for i in range(1, n+1):
    char = ''
    pwd_len = int(input('Какой длины должен быть пароль? '))
    time.sleep(1.0)
    pwd_digits = input('Включать ли в пароль цифры от 0 до 9? ')
    if pwd_digits.lower().strip() == 'да':
        char+=digits
    time.sleep(1.0)
    pwd_uppercase = input('Включать ли в пароль прописные буквы? ')
    if pwd_uppercase.lower().strip() == 'да':
        char+=uppercase_letters
    time.sleep(1.0)
    pwd_lowercase = input('Включать ли в пароль строчные буквы? ')
    if pwd_lowercase.lower().strip() == 'да':
        char+=lowercase_letters
    time.sleep(1.0)
    pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? ')
    if pwd_punctuation.lower().strip() == 'да':
        char+=punctuation
    time.sleep(1.0)
    pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')
    if pwd_exceptions.lower().strip() == 'нет':
        char+=special_symbols
    time.sleep(1.0)
    p = ''.join(random.sample(char, pwd_len))
    print(f"Ваш {i} пароль: {p}")
    list_of_pwd.append(p)
    if i!= n:
        print('Продолжаем?')
        if input().lower().strip() == 'нет':
            print(f'Список сгенерированых паролей -- {list_of_pwd}')
            print('Всего хорошего!')
            break
    else:
        print(f'Список сгенерированых паролей -- {list_of_pwd}')
        print('Всего хорошего!')
    