from math import *

n = int(input('Введите диапозон -  '))
p = [2,3]
a = 5
count = 2
while count<n:
    b = 0
    for i in range(2 , a):
        if (i <= sqrt(a)):
            if a % i == 0:
                print(a, 'непростое')
                b = 1
            else:
                pass
    if b != 1:
        print(a, 'простое')
        
        p.append(a)
    count = count + 1
    a = a + 2
print(p)
            