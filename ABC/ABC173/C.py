H, W, K = map(int, input().split())
C = []

for _ in range(H):
    C.append(list(input()))

ans = 0

for mask_h in range(2**H):
    for mask_w in range(2**W):
        block = 0
        for i in range(H):
            for j in range(W):
                if ((mask_h >> i) & 1) == 0 and ((mask_w >> j) & 1) == 0 and C[i][j] == "#":
                    block += 1
        if block == K:
            ans += 1
print(ans)
