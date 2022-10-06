x = 2 ** 1000

l = []
sum = 0
for i in range(len(str(x))):
    l.append(str(x)[i])

for i in range(len(str(x))):
    sum += int(l[i])

print(sum)