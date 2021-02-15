
s = int(input())

s_set = {s}
ai = s
i = 1
while True:
    i += 1
    if ai % 2 == 0:
        next_ai = ai//2
    else:
        next_ai = ai*3+1
    if next_ai in s_set:
        print(i)
        break
    else:
        s_set.add(next_ai)
        ai = next_ai