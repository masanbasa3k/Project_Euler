numbers = set()
for i in range(2,101):
    for j in range(2,101):
        number = i ** j
        numbers.add(number)
print(len(numbers))