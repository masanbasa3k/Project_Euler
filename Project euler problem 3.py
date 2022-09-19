#Project euler problem 3
import math 
number = 600851475143
def checkPrime(x):
    isPrime = True

    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            isPrime = False
            continue
    return isPrime

biggestPrime = 1

for i in range(2, int(math.sqrt(number))):
    if number % i == 0 and checkPrime(i):
        biggestPrime = i

print(biggestPrime)
