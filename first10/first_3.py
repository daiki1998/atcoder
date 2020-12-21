N = int(input())
A = list(map(int, input().split()))

#　解法1

# count = 0
# while True:
#     next = [a//2 for a in A if a % 2 == 0]
#     if len(next) == N:
#         count += 1
#         A = next
#     else:
#         break
# print(count)

#　解法2

count_list = []
for i in range(N):
    c = 0
    n = A[i]
    while True:
        if n % 2 == 0:
            n /= 2
            c += 1
        else:
            break
    count_list.append(c)
print(min(count_list))