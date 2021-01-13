
K = int(input())
A, B = map(int, input().split())

res = "NG"
for i in range(B+1):
    if A <= K*i <= B:
        res = "OK"
print(res)