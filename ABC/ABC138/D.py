from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
res = dict()
for i in range(1, N+1):
    res[i] = 0
for _ in range(Q):
    p, x = map(int, input().split())
    res[p] += x

done = set()
d = deque([1])
visit = [False for _ in range(N)]
while d:
    now = d.popleft()
    visit[now-1] = True
    for node in tree[now]:
        if node != now and visit[node-1] == False:
            res[node] += res[now]
            d.append(node)
print(*[v for v in res.values()])