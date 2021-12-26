import itertools

h, w, k = map(int, input().split())
feeld = [input() for _ in range(h)]
ans = 0
h_comb = []
w_comb = []


for i in range(h):
    for j in list(itertools.combinations(range(h), i)):
        h_comb.append(j)

for i in range(w):
    for j in list(itertools.combinations(range(w), i)):
        w_comb.append(j)

for h_c in h_comb:
    for w_c in w_comb:
        num=0
        for i in range(h):
            for j in range(w):
                if (i not in set(h_c)) & (j not in set(w_c)):
                    if feeld[i][j]=='#':
                        num+=1
        if num==k:
            ans+=1

print(ans)

