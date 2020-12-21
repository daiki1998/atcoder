a, b = map(int, input().split())

res = a * b

if res % 2 == 0:
    print("Even")
else:
    print("Odd")