
H, W = map(int, input().split())
A = []

min_a = 101
for i in range(H):
    A.append(list(map(int, input().split())))
    min_a = min(min_a, min(A[i]))

res = 0
for h in range(H):
    for w in range(W):
        res += A[h][w] - min_a

print(res)