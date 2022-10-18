from math import factorial

upper_limit = factorial(9)*7

sum = 0
for number in range(3, upper_limit):
    subtotal = 0
    temp = number
    
    while temp != 0:
        step  = temp % 10
        subtotal += factorial(step)
        temp //= 10

    if subtotal == number:
        sum += number
print(sum)