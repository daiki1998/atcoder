from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

d = defaultdict(int)
for s in S:
    d[s] += 1
res = []
max_num = 0
for v in d.values():
    max_num = max(max_num, v)

for k, v in d.items():
    if v == max_num:
        res.append(k)
res.sort()
for r in res:
    print(r)