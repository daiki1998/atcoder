
K = int(input())

q = [i for i in range(1,10)]

num = 0
for i in range(K):
    num = q[0]
    del q[0]
    if num % 10 != 0:
        q.append(num*10+(num%10)-1)
    q.append(num*10+(num%10))
    if num % 10 != 9:
        q.append(num*10+(num%10)+1)

print(num)