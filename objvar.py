class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0
    def __init__(self,name):
        self.name = name
        print('Создание робота {}'.format(self.name))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population+=1
    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
    def say_hi(self):
        print('Меня зовут {}'.format(self.name))
    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {} роботов.'.format(Robot.population))
    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.howMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2
Robot.howMany()

         