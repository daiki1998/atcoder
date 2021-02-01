from collections import defaultdict
import copy
N, M = map(int, input().split())
AB = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    AB[a].append(b)
    AB[b].append(a)
K = int(input())
C = list(map(int, input().split()))

res = 1
now = [C[0]]
del C[0]
flag = True
while flag:
    l = C
    can_next = AB[now[-1]]
    while True:
        next_set = set(l) & set(can_next)
        if next_set:
            next_num = list(next_set)[0]
            now.append(next_num)
            C = set(C)
            C.remove(next_num)
            C = list(C)
            res += 1
            break
        else:
            next_l = copy.deepcopy(can_next)
            for n in can_next:
                next_l += AB[n]
            res += 1
        if set(can_next) == set(next_l):
            flag = False
            break
        else:
            can_next = list(set(next_l))

    if C == []:
        break

if flag:
    print(res)
else:
    print(-1)