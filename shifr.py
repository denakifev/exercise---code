eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
print('*********Эта программа работает с шрифтом Цезаря**********')
print('Что нужно сделать? (шифрование или дешифрование)')
mes = input().lower().strip() 
if mes == 'шифрование':
    n = int(input('Введите сдвиг '))
    s = input('Введите сообщение, которое хотите зашифровать --> ')
    lan = input('Введите язык --> ')
    if lan.strip().lower() == 'русский':
        a =''
        for c in s:
            if c in rus_lower_alphabet:
                a+=rus_lower_alphabet[(rus_lower_alphabet.index(c) + n) % 32]
            elif c in rus_upper_alphabet:
                    a += rus_upper_alphabet[(rus_upper_alphabet.index(c)+n) % 32]
            else:
                a+=c
        print(f'Зашифрованное сообщение --> {a}')
    elif lan.strip().lower() == 'английский':
        a =''
        for c in s:
            if c in eng_lower_alphabet:
                a += eng_lower_alphabet[(eng_lower_alphabet.index(c) + n) % 26]
            elif c in eng_upper_alphabet:
                    a += eng_upper_alphabet[(eng_upper_alphabet.index(c)+n) % 26]
            else:
                a+=c
        print(f'Зашифрованное сообщение --> {a}')
elif mes == 'дешифрование':
    n = int(input('Введите сдвиг '))
    s = input('Введите сообщение, которое хотите дешифровать --> ')
    lan = input('Введите язык --> ')
    if lan.strip().lower() == 'русский':
        a =''
        for c in s:
            if c in rus_lower_alphabet:
                a+=rus_lower_alphabet[(rus_lower_alphabet.index(c) - n) % 32]
            elif c in rus_upper_alphabet:
                    a+= rus_upper_alphabet[(rus_upper_alphabet.index(c)-n) % 32]
            else:
                a+=c
        print(f'Дешифрованное сообщение --> {a}')
    elif lan.strip().lower() == 'английский':
        a =''
        for c in s:
            if c in eng_lower_alphabet:
                a +=eng_lower_alphabet[(eng_lower_alphabet.index(c) - n) % 26]
            elif c in eng_upper_alphabet:
                    a+= eng_upper_alphabet[(eng_upper_alphabet.index(c)-n) % 26]
            else:
                a+=c
        print(f'Дешифрованное сообщение --> {a}')
else:
    print('Простите, я вас не понимаю(')



     
