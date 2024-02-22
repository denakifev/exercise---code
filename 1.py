n, k = map(int, input().split())
coord = list(map(int, input().split()))
l = 1
r = coord[-1] - coord[0]
def good(x):
    global k 
    pos = 0
    k -= 1
    for i in range(n):
        if coord[i] - coord[pos] >= x:
            pos = i
            k -= 1
    return k <= 0
        
            
while l != r:
    mid = (l + r + 1) // 2
    if (good(mid)):
        l = mid
    else:
        r = mid - 1
print(r)
    