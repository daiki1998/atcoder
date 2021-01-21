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
N, M = map(int, input().split())
res = 0
if N >= 2:
    res += num_C_num(N, 2)
if M >= 2:
    res += num_C_num(M, 2)
print(res)