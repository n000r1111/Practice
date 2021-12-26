n = int(input())
a = [int(input()) for _ in range(n)]
now = 0
ans=0

for i in range(100000):
    now = a[now]-1
    ans += 1
    if now == 1:
        print(ans)
        exit()
        
print(-1)

