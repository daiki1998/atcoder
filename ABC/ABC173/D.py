N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
A = [0] + A

res = 0
for i in range(2, N+1):
    if i % 2 == 0:
        index = i//2
    else:
        index = i//2+1
    res += A[index]

print(res)