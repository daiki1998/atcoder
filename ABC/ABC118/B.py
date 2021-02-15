
N, M = map(int, input().split())
K, A = [], []
for _ in range(N):
    l = list(map(int, input().split()))
    K.append(l[0])
    A.append(l[1:])
res = [0 for i in range(M+1)]
for i in range(N):
    for a in A[i]:
        res[a] += 1
cnt = 0
for i in range(M+1):
    if res[i] == N:
        cnt += 1
print(cnt)