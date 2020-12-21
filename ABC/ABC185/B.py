N, M, T = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

bat = N
result = "Yes"
for i in range(M):
    if i == 0:
        not_in_cafe = A[i]
    else:
        not_in_cafe = A[i] - B[i-1]

    now_bat = bat - not_in_cafe
    if now_bat <= 0:
        result = "No"
        break
    else:
        in_cafe = B[i] - A[i]
        bat = min(N, now_bat+in_cafe)

last = T - B[-1]
last_bat = bat - last

if result == "Yes":
    if last_bat <= 0:
        result = "No"

print(result)