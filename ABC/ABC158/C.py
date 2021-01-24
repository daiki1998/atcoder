
A, B = map(int, input().split())

res = -1
for i in range(100*100):
    if int(i*0.08) == A and int(i*0.1) == B:
        res = i
        break
print(res)