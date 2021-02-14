import operator

N = int(input())
res = []
for i in range(1, N+1):
    S, P = input().split()
    res.append([i, S, 100-int(P)])
res.sort(key=operator.itemgetter(1, 2))
for i in range(len(res)):
    print(res[i][0])