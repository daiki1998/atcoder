
N = int(input())
S = input()

res = 0
cnt = 0
for i in range(N):
    if S[i] == "A":
        cnt = 1
    elif cnt == 1 and S[i] == "B":
        cnt = 2
    elif cnt == 2 and S[i] == "C":
        res += 1
        cnt = 0
    else:
        cnt = 0
print(res)
