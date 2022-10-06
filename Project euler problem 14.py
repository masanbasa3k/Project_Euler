past_numbers = dict()

def collatz(number, past_numbers):
    given = number
    steps = 1
    while number != 1:
        if number in past_numbers:
            steps += past_numbers[number] - 1
            break
        if number %2 == 0:
            number //= 2
            steps += 1
        else:
            number = 3 * number + 1
            steps += 1
    past_numbers[given] = steps
    return steps

wanted = 1
max = 1
for i in range(1, 1000001):
    move_count = collatz(i, past_numbers)
    if move_count > max:
        max = move_count
        wanted = i

print(wanted)