from itertools import permutations
a, b, k = map(int,input().split())

la = [1 for _ in range(a)]
lb = [2 for _ in range(a)]

l = la + lb

a = set(list(permutations(l)))

ans = []
for i in list(a)[k-1]:
    ans.append(chr(96 + i))

print(''.join(ans))
