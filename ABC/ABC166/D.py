
X = int(input())

i = 0
flag = True
res = []
while flag:
    num = X - i**5
    j = 0
    abs_num = abs(num)
    while abs_num + 1 > j**5:
        if abs_num == j**5:
            flag = False
            res = [i, j]
            break
        j += 1
    i += 1
if X == (res[0]**5 - res[1]**5):
    print(res[0], res[1])
else:
    print(res[0], -res[1])