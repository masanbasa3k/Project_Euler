
max_cycle = 0
divisor = 2

while divisor < 1000:
    dividend = 1
    remainders = []

    while True:
        remainder = dividend % divisor
        if remainder in remainders:
            first_index = remainders.index(remainder)
            last_index = len(remainders)
            if last_index - first_index > max_cycle:
                max_cycle = last_index - first_index
                num = divisor # we need this
            break
        dividend = 10 * remainder
        remainders.append(remainder)

    divisor += 1

print(num)