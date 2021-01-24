
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
N = int(input())
B = []
for _ in range(N):
    B.append(int(input()))
for i in range(3):
    for j in range(3):
        if A[i][j] in B:
            A[i][j] = 1000
flag = False
if sum(A[0]) == 3000 or sum(A[1]) == 3000 or sum(A[2]) == 3000:
    flag = True
if A[0][0]+A[1][0]+A[2][0] == 3000 or A[0][1]+A[1][1]+A[2][1] == 3000 or A[0][2]+A[1][2]+A[2][2] == 3000:
    flag = True
if A[0][0]+A[1][1]+A[2][2] == 3000 or A[2][0]+A[1][1]+A[0][2] == 3000:
    flag = True
if flag:
    print("Yes")
else:
    print("No")