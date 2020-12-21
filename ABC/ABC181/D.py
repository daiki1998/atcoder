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

from itertools import permutations
S = list(input())
S_int = list(map(int, S))
S_int.sort()

eight_list = []
e = 1
while e * 8 < 1000:
    if e * 8 < 100 or "0" in list(str(e*8)):
        e += 1
        continue
    eight_list.append(e*8)
    e += 1

res = "No"
if len(S) <= 2:
    for value in permutations(S):
        if int("".join(value)) % 8 == 0:
            res = "Yes"
else:
    for num in eight_list:
        S_int = sorted(list(map(int, S)))
        num_list = list(map(int, list(str(num))))
        con = 0
        for i in range(3):
            flag, index = binary_search(num_list[i], S_int)
            if flag:
                del S_int[index]
                con += 1
        if con == 3:
            res = "Yes"
print(res)