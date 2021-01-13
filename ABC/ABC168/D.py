from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

s = set(d[1]+[1])
d_res = defaultdict(int)
d_list = d[1]
for item in d[1]:
    d_res[item] = 1

while len(d_list) > 0:
    next_num = d_list[0]
    not_in = list(set(d[next_num]) - s)
    for item in not_in:
        d_res[item] = next_num
        s.add(item)
        d_list.append(item)
    del d_list[0]

d = dict(d)
d_res = dict(d_res)

if sorted(list(d_res.keys())+[1]) != sorted(list(d.keys())):
    print("No")
else:
    print("Yes")
    for i in sorted(list(d_res.keys())):
        print(d_res[i])