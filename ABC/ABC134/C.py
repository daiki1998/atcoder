
N = int(input())

A = []
for i in range(N):
    A.append(int(input()))
A_sort = sorted(A, reverse=True)
res = []
for i in range(N):
    if A_sort[0] == A[i]:
        res.append(A_sort[1])
    else:
        res.append(A_sort[0])
for i in range(N):
    print(res[i])
