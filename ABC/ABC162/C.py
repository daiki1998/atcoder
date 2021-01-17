from collections import defaultdict
import math
from functools import reduce
def gcd(l):
    return reduce(math.gcd, l)

K = int(input())

res = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            res += gcd([a, b, c])
print(res)

"""
pythonじゃ通らない
"""