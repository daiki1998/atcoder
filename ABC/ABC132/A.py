
S = input()

from collections import defaultdict

d = defaultdict(int)
for i in range(len(S)):
    d[S[i]] += 1
res = "Yes"
for v in d.values():
    if v != 2:
        res = "No"
print(res)