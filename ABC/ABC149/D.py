from collections import defaultdict

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

d = defaultdict(set)
d_plus = {"r": R, "s": S, "p": P}
res = 0
for i in range(N):
    now = T[i]
    if i + K < N:
        next_K = T[i+K]
    else:
        next_K = ""
    if next_K == "r":
        next_K = "p"
    elif next_K == "s":
        next_K = "r"
    else:
        next_K = "s"
    if now == "r":
        win = "p"
    elif now == "s":
        win = "r"
    else:
        win = "s"
    if i-K not in d[win]:
        res += d_plus[win]
        d[win].add(i)
print(res)