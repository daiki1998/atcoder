from collections import defaultdict

N = int(input())
S = " " + input()

RGB = defaultdict(list)
for i in range(1, N+1):
    RGB[S[i]].append(i)

res = len(RGB["R"]) * len(RGB["G"]) * len(RGB["B"])
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if 2*j-i <= N:
            if S[i] != S[j] and S[j] != S[2*j-i] and S[2*j-i] != S[i]:
                res -= 1
print(res)