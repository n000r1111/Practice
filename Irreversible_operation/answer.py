s = input()
ws = []
ans = 0
start = 0

for i in range(len(s)):
    if s[i]=='W':
        ws.append(i)

for i in range(len(ws)):
    ans += ws[i]-start
    start += 1

print(ans)
