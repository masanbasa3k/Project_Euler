import math

def dividingNumber(x):
    dividing = 1
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            dividing += 1
    return dividing*2

n = 1

while True:
    number = (n*(n+1))/2
    if dividingNumber(number) > 500:
        print(int(number))
        break
    n += 1
