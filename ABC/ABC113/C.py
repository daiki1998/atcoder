import operator
from collections import defaultdict

N, M = map(int, input().split())
PY = [list(map(int, input().split())) + [i] for i in range(M)]
PY.sort(key=operator.itemgetter(0, 1))

d = defaultdict(int)
for i in range(M):
    d[PY[i][0]] += 1
    PY[i].append("0"*(6-len(str(PY[i][0])))+"{}".format(PY[i][0])+"0"*(6-len(str(d[PY[i][0]])))+"{}".format(d[PY[i][0]]))
PY.sort(key=operator.itemgetter(2))
for i in range(M):
    print(PY[i][-1])