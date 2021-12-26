n = int(input())
t = list(map(int,input().split()))

starttime = sum(t) - sum(t)//2

dp = [[0]*(sum(t)+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n):
    for j in range(sum(t)+1):
        if j-t[i]>=0:
            dp[i+1][j]=dp[i][j] or dp[i][j-t[i]]
        else:
            dp[i+1][j]=dp[i][j]

for i in range(starttime, sum(t)+1):
    if dp[-1][i]:
        print(i)
        exit()


