
N = int(input())
h = list(map(int, input().split()))

h_list = [h]
res = 0
while h_list:
    now_h_list = h_list.pop()
    min_h = min(now_h_list)
    res += min_h
    index_list = []
    pre_i = 0
    for i in range(len(now_h_list)):
        now_h_list[i] -= min_h
        if now_h_list[i] == 0:
            if now_h_list[pre_i:i]:
                h_list.append(now_h_list[pre_i:i])
            pre_i = i + 1
    if now_h_list[-1] != 0 and now_h_list[pre_i:]:
        h_list.append(now_h_list[pre_i:])
print(res)