import math

def divinationSum(x):
    sum = 1
    n = 2
    while(n < math.ceil(math.sqrt(x))):
        if x % n == 0:
            sum += n
            sum += x // n
        n += 1
        if n * n == x:
            sum += n
    return sum

def control(x):
    if divinationSum(x) > x:
        return True
    else:
        return False

abundants = list()
sum = 0
sum_of_abundants = list()

for i in range(1, 28124):
    if control(i):
        abundants.append(i)

sum_of_abundants = [0]*28124

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] <= 28123:
            sum_of_abundants[abundants[i] + abundants[j]] = abundants[i] + abundants[j]

for i in range(len(sum_of_abundants)):
    if sum_of_abundants[i] == 0:
        sum += i

print(sum)