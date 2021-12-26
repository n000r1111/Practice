from itertools import combinations

n = int(input())
x = []
y = []
ans = []

for i in range(n):
    a,b = map(int,input().split())
    x.append((a,i))
    y.append((b,i))

x_sort = sorted(x)
y_sort = sorted(y)

l = []

for i in [0,1,-1,-2]:
    l.append(x_sort[i][1])
    l.append(y_sort[i][1])

for i, j in combinations(set(l),2):
    ans.append(max(abs(x[i][0]-x[j][0]),abs(y[i][0]-y[j][0])))

ans.sort()
print(ans[-2])


