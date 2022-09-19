# Project euler problem 9
done = False

for a in range(1, 1000):
    for b in range(1, 1000 - a):
        c = 1000 - a - b
        if c*c == a*a + b*b:
            print(a*b*c)
            done = True
            break
    if done:
        break