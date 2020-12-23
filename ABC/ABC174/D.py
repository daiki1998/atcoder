# 2分探索
def binary_search(num, l):
    """
    :param num: 探したい値
    :param l: リスト(ソート済み)
    :return: あるかないか(True,False)，index番号(ない場合はそのindexからnumを超える)
    """
    flag, index = False, 0
    first, last = 0, len(l)-1
    while True:
        middle = (last + first) // 2
        if num == l[middle]:
            flag, index = True, middle
            break
        elif last == first:
            if l[middle] < num: index = middle+1
            else: index = middle
            break
        elif num > l[middle]: first = min(last, middle + 1)
        elif num < l[middle]: last = max(first, middle - 1)
    return flag, index

N = int(input())
C = list(input())

R_index = []
W_index = []

for i, c in enumerate(C):
    if c == "R":
        R_index.append(i)
    else:
        W_index.append(i)

res = 0
for index in W_index:
    if len(R_index) <= 0:
        break
    flag, index = binary_search(index, R_index)
    if index < len(R_index):
        res += 1
        del R_index[-1]
print(res)