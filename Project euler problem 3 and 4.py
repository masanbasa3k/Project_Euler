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

#Project euler problem 4
def checkPalindrome(x):
    number =  str(x)
    reverseNum = number[::-1]
    if number == reverseNum:
        return True
    else:
        return False

biggestPalindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        if checkPalindrome(i*j) and i*j > biggestPalindrome:
            biggestPalindrome = i*j
print(biggestPalindrome)