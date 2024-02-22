import random
import time
def in_s(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            tmp = lst[j-1]
            lst[j-1] = lst[j] 
            lst[j] = tmp 
            j -= 1
    return lst
def buble_s(lst):
    f = 1
    for i in range(len(lst)):
        if f:
            f = 0
            for j in range(i, len(lst)):
                if lst[i] > lst[j]:
                    f = 1
                    tmp = lst[j]
                    lst[j] = lst[i]
                    lst[i] = tmp 
        else: break
    return lst

def s_s(lst):
    n = len(lst)
    for i in range(n):
        m = 1e10
        ind = -1
        for j in range(i, n):
            if lst[j] < m:
                m = lst[j]
                ind = j
        tmp = lst[ind]
        lst[ind] = lst[i]
        lst[i] = tmp
    return lst

def m_s(lst, l, r):
    if l + 1 == r:
        return [lst[l]]
    mid = (l+r) // 2
    p1 = m_s(lst, l, mid)
    p2 = m_s(lst, mid, r)
    i, j = 0, 0
    arr = []
    while i < (mid - l) and j < (r - mid):
        if p1[i] > p2[j]:
            arr.append(p2[j])
            j += 1
        elif p1[i] < p2[j]:
            arr.append(p1[i])
            i+=1
        else:
            arr.append(p1[i])
            i += 1
    while i < mid - l:
        arr.append(p1[i])
        i+=1
    while j < (r - mid):
        arr.append(p2[j])
        j += 1
    return arr
l = [10000000 - i for i in range(10)]
ch1 = time.time()
in_s(l)
ch2 = time.time()
res1 = ch2 - ch1
ch1 = time.time()
buble_s(l)
ch2 = time.time()
res2 = ch2 - ch1
ch1 = time.time()
s_s(l)
ch2 = time.time()
res3 = ch2 - ch1
ch1 = time.time()
m_s(l, 0, len(l))
ch2 = time.time()
res4 = ch2 - ch1

ch1 = time.time()
sorted(l)
ch2 = time.time()
res5 = ch2 - ch1
print(res1, res2, res3, res4, res5)


        


    