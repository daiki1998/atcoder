
N = int(input())
res = 0
for i in range(N):
    x, u = input().split()
    if u == "JPY":
        res += float(x)
    else:
        res += float(x)*380000
print(res)