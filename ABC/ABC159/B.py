
S = input()

def k(S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return False
    return True

if k(S) and k(S[:int((len(S)-1)/2)]) and k(S[int((len(S)+3)/2)-1:]):
    print("Yes")
else:
    print("No")