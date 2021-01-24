def num_C_num(n_1, n_2):
    """
    n_1Cn_2を計算
    :param n_1:
    :param n_2:
    :return: 答え
    """
    ue = 1
    shita = 1
    for i in range(n_2):
        ue *= n_1-i
        shita *= n_2-i
    return ue // shita

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
res_list = [0 for _ in range(N+1)]
for a in A:
    d[a] += 1

for k in d.keys():
    res_list[k] = num_C_num(d[k], 2)
sum_num = sum(res_list)
for k in range(N):
    print(sum_num-res_list[A[k]]+num_C_num(d[A[k]]-1, 2))