from itertools import permutations

digits = "0123456789"

numbers = list(permutations(digits))
result = numbers[999999]
result = "".join(result)

print(result)
