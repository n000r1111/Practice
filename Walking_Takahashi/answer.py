x, k, d = map(int,input().split())
ans = 0

q, mod = divmod(abs(x),d)
if mod > abs(mod-d):
   q+=1

if q<k:
    if (k-q)%2 == 0:
        ans = min(abs(x-(d*q)),abs(x+d*q))
    else:
        ans = min(abs(x-(d*q)-d),abs(x+d*q-d),abs(x-(d*q)+d),abs(x+d*q+d))   

else:
    ans = min(abs(x-(d*k)),abs(x+d*k))


print(ans)