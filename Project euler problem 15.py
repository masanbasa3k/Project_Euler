def fact(x):
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial

steps = fact(40) / (fact(20) * fact(20))
print(int(steps))