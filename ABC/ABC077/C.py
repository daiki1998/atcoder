
import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()
res = 0

for b in B:
    i_a = bisect.bisect_right(A, b-1)
    i_c = bisect.bisect_left(C, b+1)
    res += i_a * (N-i_c)

print(res)