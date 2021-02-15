
S = input()

res = 1000
for i in range(len(S)-2):
    res = min(res, abs(753-int(S[i:i+3])))
print(res)