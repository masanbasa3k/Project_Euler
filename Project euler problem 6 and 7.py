#Project euler problem 6
num = 101

def sumots(num):
    sum = 0
    for i in range(num):
        sum += i*i
    return sum

def sotsum(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum*sum

answer = sotsum(num) - sumots(num)

print(answer)

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
