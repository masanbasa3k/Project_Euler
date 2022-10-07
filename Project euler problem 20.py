import time
num = 1 
sum = 0

for i in range(1, 10001):
    num *= i

str_num = str(num)
for i in str_num:
    sum += int(i)

print(sum)