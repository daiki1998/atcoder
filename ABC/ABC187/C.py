N = int(input())
S = []
for _ in range(N):
    S.append(input())
S.sort()
index = N

for i in range(N):
    if "!" not in S[i]:
        index = i
        break
    else:
        S[i] = S[i][1:]

S_l = set(S[:index])
S_r = set(S[index:])

res = list(S_l & S_r)
if res != []:
    print(res[0])
else:
    print("satisfiable")


