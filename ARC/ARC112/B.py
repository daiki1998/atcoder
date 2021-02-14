
B, C = map(int, input().split())

if abs(B) - C//2 >= 0:
    if B >= 0:
        res = (C//2*2+1+(C-1)//2*2)
        if (abs(B) - C//2 == 0 and C % 2 == 1):
            res -= 1
    else:
        res = C//2*2+1
        if C % 2 == 1 and abs(B) - C//2 != 0:
            res += 1
    if C == 1:
        res += 1
else:
    if B == 0:
        min_num = -C//2
        max_num = (C-1)//2
    elif B > 0:
        min_num = -B-(C-1)//2
        max_num = B+(C-2)//2
    else:
        min_num = B-C//2
        max_num = -B+(C-1)//2
    res = max_num-min_num+1
print(res)