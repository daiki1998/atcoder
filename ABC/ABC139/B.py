
A, B = map(int, input().split())

res = 0
cnt = 1
while True:
    if cnt >= B:
        print(res)
        break
    else:
        cnt += A - 1
        res += 1