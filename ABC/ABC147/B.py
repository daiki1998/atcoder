
S = input()

res = 0
for i in range(len(S)//2):
    if S[i] != S[-i-1]:
        res += 1
print(res)