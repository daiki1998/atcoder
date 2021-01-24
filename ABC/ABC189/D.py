
N = int(input())
S = []
for _ in range(N):
    S.append(input())

dp = [0 for i in range(N)]

def res(i):
    if i == 1:
        if S[i-1] == "AND":
            return 1
        else:
            return 3
    elif S[i-1] == "AND":
        return res(i-1)
    else:
        return res(i-1) + 2**i


print(res(N))