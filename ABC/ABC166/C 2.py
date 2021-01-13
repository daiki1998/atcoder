from collections import defaultdict
N, M = map(int, input().split())
H = list(map(int, input().split()))
H = [0] + H
load_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    load_dict[a].append(H[b])
    load_dict[b].append(H[a])

res = 0
for i in range(1, N+1):
    if load_dict[i] == []:
        res += 1
    else:
        if H[i] > max(load_dict[i]):
            res += 1
print(res)
