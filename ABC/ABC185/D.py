N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A) | {N+1})
A.sort()

B = []

for i in range(len(A)):
    if i == 0:
        dis = A[i]-1
    else:
        dis = A[i]-A[i-1]-1
    if dis != 0:
        B.append(dis)

result = 0
if len(B) == 0:
    pass
else:
    min_dis = min(B)
    for i in range(len(B)):
        if B[i] % min_dis == 0:
            result += B[i]//min_dis
        else:
            result += B[i]//min_dis+1

print(result)