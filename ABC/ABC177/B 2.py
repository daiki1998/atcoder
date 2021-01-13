S = input()
T = input()

count = 0
for i in range(len(S)-len(T)+1):
    c = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            c += 1
    count = max(c, count)

print(len(T)-count)