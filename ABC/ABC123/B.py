
dish = []
for _ in range(5):
    dish.append(int(input()))
min_one = 9
min_index = 0
for i in range(5):
    if 0 < dish[i] % 10 <= min_one:
        min_one = dish[i] % 10
        min_index = i
res = 0
for i in range(5):
    if i == min_index or dish[i] % 10 == 0:
        res += dish[i]
    else:
        res += dish[i]//10*10+10
print(res)