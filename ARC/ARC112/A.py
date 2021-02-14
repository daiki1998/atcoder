
T = int(input())

for i in range(T):
    L, R = map(int, input().split())
    L2 = L*2
    R_2 = R // 2
    res = 0
    A_max = R
    A_min = 2*L
    if A_min > R:
        print(res)
    else:
        print((R-2*L+1)*(R-2*L+2)//2)