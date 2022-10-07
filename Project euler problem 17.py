
def num_spelled(num: int) -> int:
    d = {
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        1000: 'onethousand',
    }

    if num in d:
        return len(d[num])

    arr = []
    while num > 0:
        arr.insert(0, num%10)
        num //= 10
    output = []

    for i in range(len(arr)):
        digit = arr[i]
        if digit == 0:
            continue

        if len(arr) - i == 3: # hundreds
            output.append(d[digit])
            output.append('hundred')
            output.append('and')
        elif len(arr) - i == 2: # tens
            if digit >= 2:
                output.append(d[digit*10])
            else:
                temp = 10 + arr[i + 1]
                output.append(d[temp])
                break
        else:
            output.append(d[digit])
    if  output[-1] == 'and':
        output.pop(-1)

    return len(''.join(output))

letterCount = 0
for i in range(1, 1001):
    letterCount += num_spelled(i)

print(letterCount)

