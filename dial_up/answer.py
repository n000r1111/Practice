from collections import deque

n, m = map(int,input().split())
s = deque(map(int,input().split()))
t = deque(map(int,input().split()))

b = deque()
a = s

def shift_right(deq):
    a=deq[-1]
    deq.pop()
    deq.appendleft(a)
def shift_left(deq):
    a=deq[0]
    deq.popleft()
    deq.append(a)

i = 0
ans = 0

if n < m & set(s)!=set(t):
    print(-1)
else:
    while True:
        if b==t:
            break
        j = 0
        while True:
            if a[-j]==t[i]:
                for _ in range(j):
                    shift_right(a)
                b.append(a[0])
                ans += j+1
                i+=1
                break
            elif a[j]==t[i]:
                for _ in range(j):
                    shift_left(a)
                b.append(a[0])
                ans += j+1
                i+=1
                break
            else:
                j+=1
    print(ans)
