from itertools import combinations

n = int(input())
points = list()
ans = 0

for i in range(n):
    x,y = map(int,input().split())
    points.append((x,y))

l = [i for i in range(n)]

for i,j in combinations(l,2):
    if points[i][0]==points[j][0]:
        dif = points[i][1] - points[j][1]
        p1 = [(points[i][0] + dif, points[i][1]),(points[j][0] + dif, points[j][1])]
        p2 = [(points[i][0] - dif, points[i][1]),(points[j][0] - dif, points[j][1])]
        
        if set(points) >= set(p1):
            ans += 1
            print(p1,i,j)
        if set(points) >= set(p2):
            ans += 1
            print(p2,i,j)

    if points[i][1]==points[j][1]:
        dif = points[i][0] - points[j][0]
        p1 = [(points[i][0], points[i][1]+dif),(points[j][0], points[j][1]+dif)]
        p2 = [(points[i][0], points[i][1]-dif),(points[j][0], points[j][1]-dif)]
        if set(points) >= set(p1):
            ans += 1
            print(p1,i,j)
        if set(points) >= set(p2):
            ans += 1
            print(p2,i,j)

print(ans)