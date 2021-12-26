s = input()
length = len(s)

ans = [0]*(length+1)

for i in range(length):
    if s[i]=='<':
        ans[i+1] = ans[i]+1

for i in range(length):
    if s[length-i-1]=='>':
        if ans[length-i-1] <ans[length-i]+1:
            ans[length-i-1] = ans[length-i]+1

print(sum(ans))