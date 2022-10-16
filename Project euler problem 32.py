import itertools

numbers = [1,2,3,4,5,6,7,8,9]
permutations = list(itertools.permutations(numbers,9))

result = set()

for number in permutations:
    num1 = number[0] * 10 + number[1]
    num2 = number[2] * 100 + number[3] * 10 + number[4]
    num3 = number[5] * 1000 + number[6] * 100 + number[7] * 10 + number[8]

    if num1 * num2 == num3:
        result.add(num3)

    num1 = number[0]
    num2 = number[1] * 1000+ number[2] * 100 + number[3] * 10 + number[4]
    num3 = number[5] * 1000 + number[6] * 100 + number[7] * 10 + number[8]

    if num1 * num2 == num3:
        result.add(num3)

print(sum(result))