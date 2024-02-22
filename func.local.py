x = 50
def function(x):
   print('Значение х равно ', x)
   x = 2
   print('Замена локального х на ', x)
function(x)
print('х по-прежнему равен ', x)