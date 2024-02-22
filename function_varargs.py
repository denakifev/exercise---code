def total(a=5, *numbers, **items):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_item, second_item in items.items():
        print(first_item,second_item)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))