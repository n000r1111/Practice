n = int(input())

A = list(map(int,input().split()))

dp = [[0]*2 for _ in range(n+1)] 
dp[0][0] = 1

for i in range(n): 
    dp[i+1][0] = max(dp[i][0],dp[i][1] / A[i])
    dp[i+1][1] = max(dp[i][1],dp[i][0] * A[i])


ans = []
now = 0
for i in range(n):
    if dp[n-i][now]==dp[n-i-1][now]:
        ans.append(0)
    else:
        ans.append(1)
        if now==0:
            now = 1
        else:
            now = 0

ans.reverse()
print(*ans)


