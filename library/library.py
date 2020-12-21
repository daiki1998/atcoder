# ライブラリ系
import math
import string
from itertools import permutations, accumulate
import operator
from collections import defaultdict, Counter, deque
from functools import reduce

# 入力系
# 1つの整数を入力として受け取る
N = int(input())
# 2つ以上の整数を入力として受け取る
a, b = map(int, input().split())
# 1行の入力をlistとして受け取る
C = list(map(int, input().split()))

# 複数行に渡る2列の数字を列ごとにlistで受け取る
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

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

# 最大公約数
def gcd(l):
    """
    :param l: 最大公約数を求めたいリスト
    :return: 最大公約数
    """
    return reduce(math.gcd, l)

# 最小公倍数のbase
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

# 最上公倍数
def lcm(l):
    """
    :param l: 最小公倍数を求めたいリスト
    :return: 最小公倍数
    """
    return reduce(lcm_base, l)

# aCbを算出
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

# 約数をリストで返す
def divisor(N):
    i = 1
    l = []
    while i**2 <= N:
        if N % i == 0:
            l.append(i)
            if i**2 != N:
                l.append(N//i)
        i += 1
    return (sorted(l))