# #Project euler problem 10
import math

def prime_check(x):
    is_prime = True
    if x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                is_prime = False
                break
        return is_prime

sum = 0
number = 2

while True:
    if prime_check(number):
        sum += number
    if number == 2000000:
        break
    number += 1

print(sum)