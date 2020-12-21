N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if N > M:
    A, B = B, A
    N, M = M, N

a_num = list(set(A))

d = dict()

for a in a_num:
    d[a] = []
    for i in range(M):
        if B[i] == a:
            d[a].append(i)
    d[a].append(0)
A_B = []
now = -1
print(d)
for i in range(len(A)):
    if d[A[i]] != []:
        for j in range(len(d[A[i]])):
            if d[A[i]][j] > now:
                A_B.append(d[A[i]][j])
                now = d[A[i]][j]
                del d[A[i]][:j+1]
                break
result = len(A_B)
print(A_B)
print(M - result)