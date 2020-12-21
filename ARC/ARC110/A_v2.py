N = int(input())

l = [N]

for i in range(N-1, 1, -1):
    flag = True
    for item in l:
        if item % i == 0:
            flag = False
    if flag:
        l.append(i)

i = N + 1
result = 0

while True:
   j = 0
   while True:
       if i % l[j] == 1:
           if j == len(l)-1:
               result = i
               break
           j += 1
       else:
           i += N
           break
   if result != 0:
       break

print(result)