N, Y = map(int, input().split())

a, b, c = -1, -1, -1

for i in range(N+1):
    for j in range(N+1):
        if i*10000+j*5000+(N-i-j)*1000 == Y and N-i-j >= 0:
            a, b, c = i, j, N-i-j

print(a, b, c)