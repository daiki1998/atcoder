L = int(input())

ue = 1
shita = 1

for i in range(11):
    ue *= L-i-1
    shita *= 11-i

print(ue//shita)