
S = list(map(int, input()))
res = 0
now = S[0]
for i in range(1, len(S)):
    if abs(now-1) != S[i]:
        res += 1
    now = abs(now-1)
print(res)