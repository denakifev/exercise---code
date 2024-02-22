class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length, atleast):
        super(Exception, self).__init__()
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
# Здесь может происходить обычная работа
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введённой строки -- {0}; \
ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
except KeyboardInterrupt:
    print('Вы меня прервали меня с клавиатуры')
else:
    print('Не было исключений.')