h,w = map(int,input().split())

c = [list(input()) for _ in range(h)]

def check(x,y):
    if c[x][y]=='.':
        candidate = [str(i+1) for i in range(5)]

        if x-1>=0:
            left = c[x-1][y]
            if left in candidate:
                candidate.remove(left)
        if x+1<=h-1:
            right = c[x+1][y]
            if right in candidate:
                candidate.remove(right)
        if y-1>=0:
            up = c[x][y-1]
            if up in candidate:
                candidate.remove(up)
        if y+1<=w-1:
            down = c[x][y+1]
            if down in candidate:
                candidate.remove(down)
        return str(candidate[0])

    else:
        return c[x][y]

for i in range(h):
    for j in range(w):
        c[i][j]=check(i,j)

for i in range(h):
    print(''.join(c[i]))

