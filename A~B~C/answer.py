a, b, c = map(int,input().split())

a_1 = int(str(a)[-1])
b_1 = int(str(b)[-1])
c_1 = int(str(c)[-1])

d_1 = str(b_1**c_1)[-1]
print(str(a_1**int(d_1))[-1])