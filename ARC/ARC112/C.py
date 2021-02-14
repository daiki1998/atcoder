from collections import defaultdict
n = int(input())
p = [0, 0] + list(map(int, input().split()))

dp = defaultdict(list)
for i in range(2, n+1):
    dp[p[i]].append(i)

res = 1
tree = [1]
now = True
while tree:
    now_node = tree[0]
    del tree[0]
    if len(dp[now_node]) % 2 == 0:
        now = False