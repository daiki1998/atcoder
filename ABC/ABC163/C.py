from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

for i in range(1, N+1):
    print(d[i])