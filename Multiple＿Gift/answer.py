x, y = map(int,input().split())
ans = 0

now = x

while now <= y:
    ans+=1
    now *= 2

print(ans)
