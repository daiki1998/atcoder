A, B, C, D = map(int, input().split())

i = 0
res = ""
while True:
    if i % 2 == 0:
        C -= B
        if C <= 0:
            res = "Yes"
            break
    else:
        A -= D
        if A <= 0:
            res = "No"
            break
    i += 1
print(res)