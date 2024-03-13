# Алгоритм манакера 

s = input()
n = len(s)
d1 = [1 for i in range(n)]
l = 0 
r = 0
for i in range(1, n):
    if i < r:
        d1[i] = min(r - i + 1, d1[l + r - i])
    while i - d1[i] >= 0 and i + d1[i] < n and  s[i - d1[i]] == s[i + d1[i]]:
        d1[i] += 1
    if (i + d1[i] - 1 > r):
        l = i - d1[i] + 1
        r = i + d1[i] - 1

d2 = [0 for i in range(n)]
l = r = -1
for i in range(0, n - 1):
    if i < r:
        d2[i] = min(r - i, d2[l + r - i - 1])
    while i - d2[i] >= 0 and i + d2[i] + 1 < n and  s[i - d2[i]] == s[i + d2[i] +1]:
        d2[i] += 1
    if (i + d2[i] > r):
        l = i - d2[i] + 1
        r = i + d2[i]
print(d1, d2)

     