import sympy

def truncatable_left(x):
    number = str(x)
    flag = True
    for i in range(len(number)):
        number2 = int(number[i::])
        if sympy.isprime(number2) == False:
            flag = False
    return flag

def truncatable_right(x):
    number = str(x)
    flag = True
    for i in range(len(number)):
        number2 = int(number[:i + 1:])
        if sympy.isprime(number2) == False:
            flag = False
    return flag

number_tried = 10
truncated_numbers = []

while True:
    if sympy.isprime(number_tried) and truncatable_right(number_tried) and truncatable_left(number_tried):
        truncated_numbers.append(number_tried)
    number_tried += 1

    if len(truncated_numbers) == 11:
        break

print(sum(truncated_numbers))