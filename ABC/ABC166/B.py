N, K = map(int, input().split())
D = []
A = []
for _ in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    D.append(d)
    A.append(a)

N_sweets = [0 for _ in range(N+1)]

for k in range(K):
    for a in A[k]:
        N_sweets[a] += 1
res = 0
for i in range(1, N+1):
    if N_sweets[i] == 0:
        res += 1
print(res)