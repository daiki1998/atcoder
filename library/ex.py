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
            if l[middle] < num: index = middle
            else: index = middle-1
            break
        elif num > l[middle]: first = min(last, middle + 1)
        elif num < l[middle]: last = max(first, middle - 1)
    return flag, index
D = int(input())
N = int(input())
M = int(input())
Di = [0, D]
for _ in range(N-1):
    Di.append(int(input()))
Ki = []
for _ in range(M):
    Ki.append(int(input()))
Di.sort()
res = 0
for k in Ki:
    flag, index = binary_search(k, Di)
    if flag == False:
        res += min(abs(Di[index+1]-k), abs(k-Di[index]))
print(res)
