number = 2
numbers = []

while number < 1000000:
    temp = number
    s = 0
    while temp != 0:
        s += (temp % 10) ** 5
        temp //= 10
    if s == number:
        numbers.append(number)
    number += 1

print(sum(numbers))