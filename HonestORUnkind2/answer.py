n = int(input())

says = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    for _ in range(a):
        says[i].append(tuple(map(int,input().split())))

ans = 0

for i in range(2**n):
    choice = [True]*n
    people = [False]*n
    ok = True
    for j in range(n):
        if i >> j & 1:  
            for purson,say in says[j]:
                if choice[purson-1]:
                    people[purson-1]=say
                    choice[purson-1]=False

                else:
                    if people[purson-1]!=say:
                        ok=False
    if ok:
        ans = max(ans, sum(people))

print(ans)
    
