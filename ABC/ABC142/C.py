
N = int(input())
A = list(map(int, input().split()))

res = [0 for _ in range(N)]
for i in range(N):
    res[A[i]-1] = i+1
for i in range(N):
    print(res[i], end=" ")
print()