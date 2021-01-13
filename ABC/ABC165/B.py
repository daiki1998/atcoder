
X = int(input())

res = 100
i = 0
while True:
    i += 1
    res += res//100
    if res >= X:
        print(i)
        break