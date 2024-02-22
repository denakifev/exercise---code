def total(initial = 5 , *numbers, extra_number = 5):
    count= initial
    for keys in numbers:
        count+= keys
    count+=extra_number
    print(count)
total(10, 1, 3, 5 ,4, 3 , extra_number = 34)
total(10, 7,8,9,50)
