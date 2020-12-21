
X, Y, A, B = map(int, input().split())

count = 0

while True:
    if X * (A-1) < B:
        if X * A >= Y:
            break
        else:
            X *= A
            count += 1
    else:
        can_up = Y - X - 1
        count += can_up // B
        break
print(count)