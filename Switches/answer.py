import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())


lights = [list(map(lambda x:int(x)-1, input().split()))[1:]
         for _ in range(m)]

p = list(map(int,input().split()))
ans = 0

for i in range(2 ** n):
    for num in range(m):
        up=0
        for j in range(n):  
            if i >> j & 1 and j in lights[num]:
                up+=1
        if up % 2 != p[num]:
            break

    else:
        ans += 1
            
        

print(ans)

            

