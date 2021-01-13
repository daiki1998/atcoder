
import operator

N, C = map(int, input().split())
res_list = []
B = []
for i in range(N):
    a, b, c = map(int, input().split())
    res_list.append([a, c])
    res_list.append([b+1, -c])
    B.append(b)

res_list = sorted(res_list, key=operator.itemgetter(0))
res = 0
now_cost = 0
max_B = max(B)
for i in range(len(res_list)):
    if res_list[i][0] == max_B+1:
        break
    now_time, cost = res_list[i]
    next_time = res_list[i+1][0]
    now_cost += cost
    res += min(now_cost, C)*(next_time-now_time)
print(res)