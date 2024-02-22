number=34
running=True
print(
    '''Я загадал число.
Попробуй его угадать!'''
)
while running:
    guest=int(input(
        'Введите число '
    ))
    if number==guest:
        print('Поздравляю, вы выиграли.')
        print( 'Хотя и не получили никакого приза')
        running=False
    elif guest<number:
        print('Ваше число немного меньше')
    else: print('Ваше число немного больше')
else: print('Цикл while окончен')
print('Конец игры')
    
           
        