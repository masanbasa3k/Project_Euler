# Project euler problem 7
import math

def prime_check(x):
    is_prime =True

    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            is_prime = False
            continue
    return is_prime

prime_count = 0
number = 2

while True:
    if prime_check(number):
        prime_count += 1
    if prime_count == 10001:
        print(number)
        break
    number += 1
