
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

res_list = [1]
next_index = 1
s = {1}
for i in range(N):
    next_index = A[next_index]
    res_list.append(next_index)
    if next_index in s:
        break
    else:
        s.add(next_index)

search_num = res_list[-1]
index = 0
for i in range(len(res_list)):
    if search_num == res_list[i]:
        index = i
        break

rep_list = res_list[index:-1]
if len(res_list)-1 < K:
    print(rep_list[(K-index+1)%(len(rep_list))-1])
else:
    print(res_list[K])
