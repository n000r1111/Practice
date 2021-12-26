import math

n = int(input())

change = []
now = 2

while n**(1/now) >= 2:
    change.append(int(math.pow(n,1/now)+1))
    now += 1


can_num = set()

for i in range(len(change)):
    for j in range(2,change[i]+1):
        if j**(i+2)<=n:
            can_num.add(j**(i+2))

print(n-len(can_num))


