from collections import defaultdict

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

N = int(input())

res = defaultdict(int)
cnt = 0
for i in range(N):
    res_s = defaultdict(int)
    s = list(input())
    s.sort()
    for j in range(len(s)):
        res_s[s[j]] += 1
    r = ""
    for k, v in res_s.items():
        r += (str(k)+str(v))
    res[r] += 1
for key in res.keys():
    cnt += num_C_num(res[key], 2)
print(cnt)