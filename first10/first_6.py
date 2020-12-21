N = int(input())
A = list(map(int, input().split()))

a = 0
b = 0
A.sort(reverse=True)
flag = "a"
while True:
    if A == []:
        break
    if flag == "a":
        a += A[0]
        del A[0]
        flag = "b"
    else:
        b += A[0]
        del A[0]
        flag = "a"

"""
print(sum(A[::2])-sum(A[1::2]))
"""

print(a-b)