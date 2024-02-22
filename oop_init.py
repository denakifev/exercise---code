class Person:
    def __init__(self,name): #Инициализируем данные(имя) объекта класса 
        self.name = name 
    def sayme(self):
        print('Мое имя {}'.format(self.name))

p = Person("Алексей")
p.sayme()