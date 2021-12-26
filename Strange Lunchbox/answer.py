import math

n = int(input())
x, y = map(int,input().split())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i],b[i] = map(int,input().split())


dp = [[[math.inf]*(sum(b)+1)]* (sum(a)+1) for _ in range(n+1)]
dp[0][0][0]=1

for i in range(n):
    for j in range(sum(a)+1):
        for k in range(sum(b)+1):
            if j-a[i]>=0 and k-b[i]>=0:
                dp[i+1][j][k] = dp[i][j][k] or dp[i][j-a[i]][k-b[i]]
            else:
                dp[i+1][j][k] = dp[i][j][k]

            if dp[i+1][j][k]:
                if j>=x and k>=y:
                    print(i)
                    exit()
print(-1)
