
N, K, Q = map(int, input().split())
res = [0 for _ in range(N)]
for _ in range(Q):
    a = int(input())
    res[a-1] += 1
for i in range(N):
    point = K - (Q - res[i])
    if point <= 0:
        print("No")
    else:
        print("Yes")