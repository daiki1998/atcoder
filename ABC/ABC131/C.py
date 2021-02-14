# 最小公倍数のbase
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

A, B, C, D = map(int, input().split())

can_C = B//C - (A-1)//C
can_D = B//D - (A-1)//D
C_D = lcm([C, D])
can_C_D = B//C_D - (A-1)//C_D
print(B-A-(can_C+can_D-can_C_D)+1)