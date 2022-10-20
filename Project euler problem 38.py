pandigitals = []
mset = set('123456789')

for i in range(1, 10_000):
    step = 1
    strnumber = ''
    while True:
        number = i * step
        strnumber += str(number)
        if len(strnumber) >= 9:
            if len(strnumber) > 9:
                break
            else:
                if set(strnumber) == mset:
                    pandigitals.append(int(strnumber))
                    break

        step += 1

print(max(pandigitals))