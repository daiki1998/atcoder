
N = int(input())
S = input()

res = 0
now = ""
for i in range(N):
    if S[i] != now:
        now = S[i]
        res += 1
print(res)