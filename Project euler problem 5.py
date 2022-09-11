# Project euler problem 5
import math
import functools

def gcd(x, y):
    return math.gcd(x, y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

L = range(1, 21)

result = functools.reduce(lcm, L)
print(result)