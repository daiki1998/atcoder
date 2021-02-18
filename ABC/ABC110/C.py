from collections import defaultdict

S = input()
T = input()

res = "Yes"
d = defaultdict(list)
d_rev = defaultdict(list)
for i in range(len(S)):
    d[S[i]].append(T[i])
    d_rev[T[i]].append(S[i])
    d[S[i]] = list(set(d[S[i]]))
    d_rev[T[i]] = list(set(d_rev[T[i]]))
    if len(d[S[i]]) > 1 or len(d_rev[T[i]]) > 1:
        res = "No"

print(res)

