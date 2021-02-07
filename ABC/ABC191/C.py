
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

res = 0
for h in range(H-1):
    for w in range(W-1):
        cnt = 0
        for i in range(2):
            for j in range(2):
                if S[h+i][w+j] == "#":
                    cnt += 1
        if cnt == 1 or cnt == 3:
            res += 1

print(res)