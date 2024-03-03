s = input()
t = input()
s = t + '#' + s
pref = [0 for i in range(len(s))]
for i in range(1, len(s)):
    j = pref[i-1]
    while  j > 0 and s[j] != s[i]:
        j = pref[j - 1]
    if s[j] == s[i]:
        pref[i] = j + 1
    else:
        pref[i] = 0

for i in range(len(t) + 1, len(s)):
    if pref[i]== len(t):
        print(i - 2 * len(t), end=' ')