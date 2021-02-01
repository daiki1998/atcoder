
N = int(input())
X = list(map(int, input().split()))

mean = sum(X)//len(X)
res_1 = 0
res_2 = 0
for i in range(N):
    res_1 += (X[i]-mean)**2
    res_2 += (X[i]-mean-1)**2
print(min(res_1, res_2))