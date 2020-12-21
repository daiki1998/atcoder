N, T = map(int, input().split())
A = list(map(int, input().split()))

B = A[:len(A)//2]
C = A[len(A)//2:]
napB = set([0])
napC = set([0])

for i in range(len(B)):
    nap_list = list(napB)
    nap_list += [n + B[i] for n in nap_list if n + B[i] <= T]
    napB = set(nap_list)

for i in range(len(C)):
    nap_list = list(napC)
    nap_list += [n + C[i] for n in nap_list if n + C[i] <= T]
    napC = set(nap_list)

D = list(napB)
E = list(napC)
D.sort()
E.sort()

# print(D)
# max = 0
for i in range(len(E)):
    nap_list = list(napB)
    nap_list += [n + E[i] for n in nap_list if n + E[i] <= T]
    napB = set(nap_list)
    #
    #
    # for j in range(len(E)):
    #     if D[i] + E[j] <= T and D[i] + E[j] > max:
    #         max = D[i] + E[j]

# print(max)
print(max(list(napB)))