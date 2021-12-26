n, m = map(int,input().split())

ab = [list(map(int,input().split())) for _ in range(m)]

p = [-1]*(n+1)

p[0]=0

def find(x):
    if p[x] == -1:
        return x
    else:
        p[x]=find(p[x])
        return p[x]

def unite(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        p[y]=x

ans = 0

for i in range(m):
    for j in range(m):
        if i != j:
            unite(ab[j][0],ab[j][1])

    if p.count(-1) > 1:
        ans += 1

    p = [-1]*(n+1)
    p[0]=0

print(ans)
