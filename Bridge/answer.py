n, m = map(int,input().split())

ab = [list(map(int,input().split())) for _ in range(m)]

p = [-1]*(n+1)

def find(x):
    if p[x] < 0:
        return x
    else:
        p[x]=find(p[x])
        return p[x]

def unite(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return 0
    else:
        if p[x] > p[y]:
            x,y = y,x
        p[x] += p[y]
        p[y] = x 
        

def size(x):
    return -p[find(x)]

def same(x,y):
    return find(x) == find(y)

ans = []
convenient = int(n*(n-1)/2)

ab.reverse()

for i in range(m):
    ans.append(convenient)
    

    a = ab[i][0]
    b = ab[i][1]

    size_a = size(a)
    size_b = size(b)

    if same(a,b)==False:
        convenient -= size_a*size_b
        unite(a, b)

ans.reverse()  

for i in ans:
    print(i)
    







