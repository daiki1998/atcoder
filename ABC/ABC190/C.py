
N, M = map(int, input().split())
A, B, C, D = [], [], [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
K = int(input())
for _ in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

res = 0
for i in range(2**K):
    num_list = [0 for _ in range(0, N+1)]
    for j in range(K):
        if ((i >> j) & 1):
            num_list[C[j]] += 1
        else:
            num_list[D[j]] += 1
    cnt = 0
    for m in range(M):
        if num_list[A[m]] > 0 and num_list[B[m]] > 0:
            cnt += 1
    res = max(res, cnt)
print(res)

