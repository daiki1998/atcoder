N, M, X = map(int, input().split())

C = []
A = []

for i in range(N):
    inp = list(map(int, input().split()))
    C.append(inp[0])
    A.append(inp[1:])

min_cost = 12 * 10**5 + 1
for i in range(2**N+1):
    cost = 0
    A_sum = [0 for _ in range(M)]
    for j in range(N):
        if (i >> j) & 1:
            cost += C[j]
            A_sum = [A_sum[k]+A[j][k] for k in range(M)]
    m_num = 0
    for m in range(M):
        if A_sum[m] >= X:
            m_num += 1
    if m_num == M:
        min_cost = min(min_cost, cost)

if min_cost == 12 * 10**5 + 1:
    print(-1)
else:
    print(min_cost)