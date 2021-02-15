
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_num = 10**9
res = -1
for i in range(N):
    if min_num >= abs(A-(T-H[i]*0.006)):
        min_num = abs(A-(T-H[i]*0.006))
        res = i+1
print(res)