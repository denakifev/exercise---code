def Printmax(a,b):
    if a < b:
        return b
    elif a > b :
        return a
    else: return "числа равны"
a = int(input())
b = int(input())
print(Printmax(a, b))