
ant = []
for i in range(6):
    ant.append(int(input()))

res = "Yay!"
for i in range(5):
    for j in range(i+1, 5):
        if abs(ant[i]-ant[j]) > ant[-1]:
            res = ":("
print(res)