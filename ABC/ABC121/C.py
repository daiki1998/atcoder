import operator

N, M = map(int, input().split())
A_B = [list(map(int, input().split())) for _ in range(N)]
A_B.sort(key=operator.itemgetter(0))

i = 0
res = 0
while True:
    if A_B[i][1] >= M:
        res += A_B[i][0]*M
        break
    else:
        res += A_B[i][0]*A_B[i][1]
        M -= A_B[i][1]
    i += 1
print(res)