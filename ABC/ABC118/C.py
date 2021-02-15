
# 最大公約数
import math
from functools import reduce
def gcd(l):
    """
    :param l: 最大公約数を求めたいリスト
    :return: 最大公約数
    """
    return reduce(math.gcd, l)

N = int(input())
A = list(map(int, input().split()))

A = list(set(A))
print(gcd(A))