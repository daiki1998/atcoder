from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for _ in range(M):
    s, c = map(int, input().split())
    d[s].append(c)

res = -1
if len(set(d[1])) > 1 or len(set(d[2])) > 1 or len(set(d[3])) > 1:
    pass
elif d[1] == [0]:
    pass
else:
    res = ""
    for i in range(1, N+1):
        if d[i] != []:
            res += str(d[i][0])
        else:
            res += "0"
    res = int(res)
print(res)