n = int(input())
A = list(map(int,input().split()))

dp = [0]*(n+1)
dp1 = [0]*(n+1)

for i in range(n):
    dp[i+1]=dp[i]+A[i]

for i in range(n):
    dp1[i+1]=max(dp1[i],dp[i]+A[i])

dp2 = [0]*(n+1)

for i in range(n):
    dp2[i+1]=dp2[i]+dp[i+1]

dp3 = [0]*(n+1)
for i in range(1,n+1):
    dp3[i] = dp2[i-1] + dp1[i]

print(max(dp3))