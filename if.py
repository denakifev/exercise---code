#!/usr/bin/env python3
number=37
guest=int(input('Введите число: '))
if number == guest:
    print('Поздравляю, вы выиграли!')
    print('Хотя и не получили никакого приза')
elif number<guest:
    print('Ваше число немного больше загаданного')
else: print('Ваше число немного меньше загаданного')
print('Конец игры')
