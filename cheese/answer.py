from collections import deque
que = deque()
h, w, n = map(int,input().split())
graph = [input() for _ in range(h)]

dxdy = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(h):
    for j in range(w):
        if graph[i][j]=='S':
            start = [i,j]

arrived = [[True]*w for _ in range(h)]

counter = [0] * n

que.append(start)


distance = 0
while que:
    distance += 1
    now = que.popleft()

    for x,y in dxdy:
        next_x = now[0]+x
        next_y = now[1]+y
        if next_x >= 0 & next_x < w & next_y >= 0 & next_y < h:
            if arrived[next_x][next_y]:
                if graph[next_x][next_y]=='.':
                    arrived[next_x][next_y] = False
                    que.append([next_x, next_y])
                elif graph[next_x][next_y]=='X':
                    arrived[next_x][next_y] = False
                else:
                    counter[int(graph[next_x][next_y])-1]+=distance
                    arrived[next_x][next_y] = False
                    que.append([next_x, next_y])
print(*counter)

