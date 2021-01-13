import operator

N = int(input())
A_B = []
for i in range(N):
    a, b = map(int, input().split())
    if a <= b:
        A_B.append([a, b])
    else:
        A_B.append([b, a])

A_B = sorted(A_B, key=operator.itemgetter(0, 1))
print(A_B)
res = 0
s = set()

for i in range(N):
    if A_B[i][0] not in s:
        res += 1
        s = set(list(s) + [A_B[i][0]])
    elif A_B[i][1] not in s:
        res += 1
        s = set(list(s) + [A_B[i][0]])
print(s)
print(res)