s = input()

length=len(s)
ans = 0

for i in range(length):
    ans += (length-1-i)*(10**i)

