n = int(input())

s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

spoint = []
tpoint = []

for i in range(n):
    for j in range(n):
        if s[i][j]=='#':
            spoint.append((i,j))
        if t[i][j]=='#':
            tpoint.append((i,j))

def turn(s):
    turn_s = []
    for i,j in s:
        turn_s.append((j,n-1-i))
    
    return turn_s

spoint_1 = turn(spoint)
spoint_2 = turn(spoint_1)
spoint_3 = turn(spoint_2)


if set(spoint)==set(tpoint):
    print('Yes')
elif set(spoint_1)==set(tpoint):
    print('Yes')
elif set(spoint_2)==set(tpoint):
    print('Yes')
elif set(spoint_3)==set(tpoint):
    print('Yes')
else:
    print('No')

