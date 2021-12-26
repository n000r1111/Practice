MOD = 998244353


n = int(input())
a = list(map(int,input().split()))

dp = [[0]*10 for i in range(n)]


dp[0][a[0]]=1

for i in range(n-1):
    for j in range(10):
        dp[i+1][(j+a[i+1])%10] += dp[i][j]
        dp[i+1][(j*a[i+1])%10] += dp[i][j]
        dp[i+1][(j+a[i+1])%10] %= MOD
        dp[i+1][(j*a[i+1])%10] %= MOD
        

for i in dp[n-1]:
    print(i)