N, W = map(int, input().split())
S, T, P = [], [], []
for _ in range(N):
    s, t, p = map(int, input().split())
    S.append(s)
    T.append(t)
    P.append(p)

table = [0 for i in range(max(T)+1)]
for i in range(N):
    table[S[i]] += P[i]
    table[T[i]] -= P[i]

for i in range(1, len(table)):
    table[i] += table[i-1]

if max(table) > W:
    print("No")
else:
    print("Yes")