def convert_to_base_two(x):
    remainders = []
    while x != 0:
        remainder = x % 2
        remainders.append(str(remainder))
        x //= 2
    result = ''.join(remainders)[::-1]
    return result

num = 1
sum = 0

while num < 1_000_000:
    if str(num) == str(num)[::-1] and convert_to_base_two(num) == convert_to_base_two(num)[::-1]:
        sum += num
    num += 1
print(sum)