#Project euler problem 6
num = 101

def sumots(num):
    sum = 0
    for i in range(num):
        sum += i*i
    return sum

def sotsum(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum*sum

answer = sotsum(num) - sumots(num)

print(answer)

