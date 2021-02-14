
N, K = map(int, input().split())
S = input()

res = ""
d = {"A":"a", "B":"b", "C":"c"}
for i in range(N):
    if K-1 == i:
        res += d[S[i]]
    else:
        res += S[i]
print(res)