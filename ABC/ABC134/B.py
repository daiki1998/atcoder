N, D = map(int, input().split())

num = D*2+1
if N % num == 0:
    print(N//num)
else:
    print(N//num+1)