from itertools import permutations
import math

N = int(input())
X_Y = []
for _ in range(N):
    X_Y.append(list(map(int, input().split())))

res = 0
o_list = [i for i in range(N)]
for o in list(permutations(o_list)):
    i = o[0]
    res_now = 0
    for j in o[1:]:
        xi, yi = X_Y[i]
        xj, yj = X_Y[j]
        res_now += math.sqrt((xi-xj)**2+(yi-yj)**2)
        i = j
    res += res_now
print(res/len(list(permutations(o_list))))