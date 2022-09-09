# #Project euler problem 1
sum = 0
for i in range(1000):
    if i%5 == 0 or i%3 == 0:
        sum += i
print(sum)

# #Project euler problem 2
l=[1,2]
i = 2
while True:
    if l[i-1]+l[i-2]< 4000000:
        l.append(l[i-1]+l[i-2])
        i+=1
    else: break

sum = 0
for i in l:
    if i % 2 == 0:
        sum += i
print(sum)