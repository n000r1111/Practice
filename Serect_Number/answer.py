import itertools

s = input()

use = []
no_use = []

for i in range(len(s)):
    if s[i]=='o':
        use.append(str(i))
    elif s[i]=='x':
        no_use.append(str(i))
    else:
        pass

ans = 0

for i in range(10000):
    s = str(i).zfill(4)
    a = True
    for j in use:
        if j not in s:
            a = False
            
    for k in no_use:
        if k in s:
            a = False
    if a:        
        ans += 1

print(ans)