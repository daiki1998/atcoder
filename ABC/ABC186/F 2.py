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
H, W, M = map(int, input().split())
X, Y = [], []
dict_H = {}
dict_W = {}
for i in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    X.append(x)
    if x in dict_H.keys():
        dict_H[x].append(y)
    else:
        dict_H[x] = [y]
    if y in dict_W.keys():
        dict_W[y].append(x)
    else:
        dict_W[y] = [x]

res = 0
for h in range(H):
    if h in dict_H.keys():
        res += sorted(dict_H[h])[0]
    else:
        res += W
blo = [H]
for w in range(W):
    if w in dict_W.keys():
        dict_W[w].sort()
        a = dict_W[w][0]
        res += dict_W[w][0]
        flag, index = binary_search(dict_W[w][0], blo)
    else:
        a = H
        res += H
        flag, index = binary_search(W, blo)
    if blo != [H]:
        res -= len(blo[:index+1])

    print(index, blo[index], blo, a)
    if w in dict_W.keys():
        blo = list(set(blo + dict_W[w]))


print(res)