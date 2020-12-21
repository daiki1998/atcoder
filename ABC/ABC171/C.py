import string
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

a = [0, 26]
i = 2
while True:
    if a[-1] > 1000000000000001:
        break
    a.append(a[-1]+26**i)
    i += 1

flag, index = binary_search(N, a)
l = []
num = N - a[index-1]
for i in range(index):
    if num == 0:
        l.append(1)
    elif num % 26 == 0:
        l.append(26)
        num //= 26
    else:
        l.append(num%26)
        num = num // 26 + 1

abc = [""] + list(string.ascii_lowercase)
alp = ""
l.reverse()
for i in range(len(l)):
    alp += abc[l[i]]
print(alp)
