from collections import defaultdict

n, k = map(int,input().split())
c = list(map(int,input().split()))

mp = defaultdict(int)
ans = 0
now = 0

for i in range(n):
    if mp[c[i]]==0:
        now += 1
    mp[c[i]]+=1

    if i>=k:
        mp[c[i-k]]-=1
        if mp[c[i-k]]==0:
            now -= 1

    ans = max(ans, now)

print(ans)