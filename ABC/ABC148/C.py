import math
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

# 最上公倍数
def lcm(l):
    """
    :param l: 最小公倍数を求めたいリスト
    :return: 最小公倍数
    """
    return reduce(lcm_base, l)

A, B = map(int, input().split())

print(lcm([A, B]))
