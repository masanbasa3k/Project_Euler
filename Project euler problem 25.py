
a = 1
b = 1

step = 2

while True:
    a, b = b, a + b
    step += 1
    if len(str(b)) == 1000:
        print(step)
        break