
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
res = 0
for n in range(N):
    cnt = 0
    for i in range(M):
        cnt += A[n][i]*B[i]
    if cnt+C > 0:
        res += 1
print(res)