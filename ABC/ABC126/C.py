import bisect

N, K = map(int, input().split())

res = 0
two = [1]
two_num = 1
while two_num < 10**5:
    two_num *= 2
    two.append(two_num)

for i in range(1, N+1):
    x = (K/i)
    index = bisect.bisect_left(two, x)
    res += (1/N)*(1/2)**index
print(res)