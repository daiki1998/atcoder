from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B, C = [], []
for _ in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

A_dict = defaultdict(int)
for i in range(len(A)):
    A_dict[A[i]] += 1
res = 0
for k, v in A_dict.items():
    res += k*v

for i in range(Q):
    A_dict[C[i]] += A_dict[B[i]]
    res += (C[i]*A_dict[B[i]]-B[i]*A_dict[B[i]])
    A_dict[B[i]] = 0
    print(res)