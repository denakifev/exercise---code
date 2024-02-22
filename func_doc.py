def func(a,b):
    '''Выводит максимальное из двух чисел.
    
    Оба числа должны быть целыми.'''
    
    a = int(a)
    b = int(b)
    if a<b:
        print(b, " наибольшее")
    elif b<a:
        print (a, ' наибольшее')
    else: print ('числа равны')
    
func( 3, 17)
print (func.__doc__)



