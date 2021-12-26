n = int(input())
ans = []

while True:
    if n<=26:
        ans.append(n)
        break

    q, mod = divmod(n,26)
    
    if mod == 0:
        q-=1
        mod=26
    n = q
    ans.append(mod)

ans.reverse()

for i in range(len(ans)):
    if i==len(ans)-1:
        print(chr(96+ans[i]))
    else:
        print(chr(96+ans[i]),end='')
