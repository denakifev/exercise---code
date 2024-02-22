from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration
    def __iter__(self):
        return self # метод возвращает сам объект 

for x in RandomIterator(4):
    print(x) 


# Еще один пример 

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i +=2
            return self.lst[self.i- 2], self.lst[self.i-2]
        else:
            raise StopIteration

class Mylist(list):
    def __iter__(self):
        return DoubleElementListIterator(self) # Используем экземпляр класса итератора 

for pair in Mylist([1,2,3,4,5,6]):
    print(pair)
