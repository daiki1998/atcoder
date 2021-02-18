
# 最大公約数
import math
from functools import reduce
def gcd(l):
    """
    :param l: 最大公約数を求めたいリスト
    :return: 最大公約数
    """
    return reduce(math.gcd, l)


N, X = map(int, input().split())
x = list(map(int, input().split()))

l = []
for i in range(N):
    l.append(abs(x[i]-X))
print(gcd(l))