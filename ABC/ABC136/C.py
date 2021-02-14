
N = int(input())
H = list(map(int, input().split()))

res = "Yes"
pre = H[-1]

for i in range(N-1, -1, -1):
    if pre >= H[i]:
        pre = H[i]
    else:
        if pre == H[i] - 1:
            pre = H[i] - 1
        else:
            res = "No"
print(res)