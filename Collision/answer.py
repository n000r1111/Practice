from collections import deque
import math

n, q = map(int,input().split())

route = [[] for _ in range(n)]

for i in range(n-1):
    x,y = map(int,input().split())
    route[x-1].append(y-1)
    route[y-1].append(x-1)

cd = [list(map(int,input().split())) for _ in range(q)]

seen = [False]*n
distance = [math.inf]*n
distance[0]=0
d = deque()
d.append(0)

while d:
    head = d.popleft()
    seen[head]=True
    for i in route[head]:
        if seen[i]==False:
            d.append(i)
            distance[i]=distance[head]+1

for i in range(q):
    if abs(distance[cd[i][0]-1]-distance[cd[i][1]-1])%2 == 0:
        print('Town')
    else:
        print('Road')