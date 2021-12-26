from collections import deque

n, q = map(int,input().split())
connect = [[] for i in range(n)]

p = [0]*q
x = [0]*q

for i in range(n-1):
    a,b = map(lambda t:int(t)-1,input().split())
    connect[a].append(b)
    connect[b].append(a)

counter = [0] * n
visited = [True] * n
visited[0]=False

for i in range(q):
    p,x = map(int,input().split())
    counter[p-1]+=x

que = deque([0])

que.append(0)

while que:
    now = que.popleft()
    now_number = counter[now]

    for i in connect[now]:
        if visited[i]:
            counter[i]+=now_number
            visited[i]=False
            que.append(i)

print(*counter)


    