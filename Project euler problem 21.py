
def d(x):
    div_list = list()
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            div_list.append(i)
    return sum(div_list)

amicables = list()
for i in  range(1, 10001):
    if d(d(i)) == i and i != d(i):
        amicables.append(i)

print(sum(amicables))