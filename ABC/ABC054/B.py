import math

P = float(input())

def calc(t):
    return t + P * 2 ** (-t/1.5)

l, r = 0, P
while r - l > 10**(-8):
    c1 = (l+l+r)/3
    c2 = (l+r+r)/3
    if calc(c1) < calc(c2):
        r = c2
    else:
        l = c1
print(calc(l))