x = 30
def function():
    global x
    print('Значение х состовляет', x)
    x = 2
    print("замена глобального х на ", x)
function()
print("новое значение х состовляет" , x)