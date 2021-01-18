
N, M = map(int, input().split())
k = []
s = []
for _ in range(M):
    l = list(map(int, input().split()))
    k.append(l[0])
    s.append(l[1:])
p = list(map(int, input().split()))

res = 0
for i in range(2**N):
    cnt_m = 0
    for j in range(M):
        bin_i = i
        cnt_s = 0
        for m in range(N):
            if ((bin_i >> m) & 1) and m+1 in s[j]:
                cnt_s += 1
        if cnt_s % 2 == p[j]:
            cnt_m += 1
    if cnt_m == M:
        res += 1

print(res)