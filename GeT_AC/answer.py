n,q = map(int,input().split())
s = input()

for i in range(q):
    l, r = map(int,input().split())
    a = ''.join(list(s)[l-1:r])
    print(a.count('AC'))