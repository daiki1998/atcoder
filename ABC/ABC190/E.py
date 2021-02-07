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
    back = copy.deepcopy(C)
    forward = AB[now[-1]]
    while True:
        can_go = set(back) & set(forward)
        if can_go:
            if can_go & set(C):
                next_num = list(can_go & set(C))[0]
                now.append(next_num)
            else:
                while True:
                    res += 1
                    now.append("A")
                    can_go_go = copy.deepcopy(list(can_go))
                    for n in can_go:
                        can_go_go += AB[n]
                    if set(can_go_go) & set(C):
                        next_num = list(set(can_go_go) & set(C))[0]
                        now.append(next_num)
                        break
            C = set(C)
            C.remove(next_num)
            C = list(C)
            res += 1
            break
        else:
            now.append("A")
            next_forward = copy.deepcopy(forward)
            next_back = copy.deepcopy(back)
            for n in forward:
                next_forward += AB[n]
            for n in back:
                next_back += AB[n]
            res += 1
        if set(next_forward) == set(forward) and set(next_back) == set(back):
            flag = False
            break
        else:
            forward = list(set(next_forward))
            back = list(set(next_back))
    if C == []:
        break
if flag:
    print(res)
else:
    print(-1)