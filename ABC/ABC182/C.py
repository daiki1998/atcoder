N = int(input())

amari = N % 3
res = -1
keta = len(str(N))

if amari == 0:
    res = 0
elif amari == 1:
    count = [0, 0]
    for i in range(keta):
        if (N % 10) % 3 == 1:
            count[0] += 1
        elif (N % 10) % 3 == 2:
            count[1] += 1
        N = N // 10
    if count[0] >= 1 and keta > 1:
        res = 1
    elif count[1] >= 2 and keta > 2:
        res = 2
elif amari == 2:
    count = [0, 0]
    for i in range(keta):
        if (N % 10) % 3 == 1:
            count[0] += 1
        elif (N % 10) % 3 == 2:
            count[1] += 1
        N = N // 10
    if count[1] >= 1 and keta > 1:
        res = 1
    elif count[0] >= 2 and keta > 2:
        res = 2
print(res)