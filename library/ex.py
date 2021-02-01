from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
for i in range(N):
    k_v = list(map(int, input().split()))
    if k_v[1] != 0:
        for e in k_v[2:]:
            graph[k_v[0]].append(e)
res = {1: 0}
for i in range(2, N+1):
    res[i] = -1
s = set()
s.add(1)
node = deque([1])
while len(node) > 0:
    now = node.popleft()
    for n in graph[now]:
        if n not in s:
            node.append(n)
            s.add(n)
            res[n] = res[now] + 1

for i in range(1, N+1):
    print(i, res[i])