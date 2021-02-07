from collections import defaultdict

N, M = map(int, input().split())
flag = False
res_wa = 0
res_ac = 0
wa = defaultdict(int)
res = defaultdict(int)
for i in range(M):
    p, S = input().split()
    p = int(p)
    if res[p] == 1:
        continue
    else:
        if S == "WA":
            wa[p] += 1
        else:
            res[p] += 1
for k in res.keys():
    if res[k] == 1:
        res_wa += wa[k]
        res_ac += res[k]
print(res_ac, res_wa)