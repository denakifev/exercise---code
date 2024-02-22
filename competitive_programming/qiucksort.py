import random as r

l = [r.randint(1,100) for i in range(21)]

def quicksort(array):
    if len(array) < 2:
        return array 
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(l)
print(quicksort(l))
    