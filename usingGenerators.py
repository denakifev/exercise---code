from random import random

def RandomGenerator(k):
    for i in range(k):
        yield random()

gen = RandomGenerator(10)
for i in gen:
    print(i)

def SimpleGenerator():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    return 'No more elements'
    # yield 2
    # print('Checkpoint 3') Данная часть функции будет недостижима


x = SimpleGenerator()

print(next(x))
print(next(x))

