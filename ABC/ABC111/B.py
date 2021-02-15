
N = int(input())

i = N
while True:
    if len(set((str(i)))) == 1:
        print(i)
        break
    i += 1