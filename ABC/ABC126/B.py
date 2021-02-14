
S = input()

f = True if 0 < int(S[:2]) < 13 else False
b = True if 0 < int(S[2:]) < 13 else False

if f and b:
    print("AMBIGUOUS")
elif f:
    print("MMYY")
elif b:
    print("YYMM")
else:
    print("NA")