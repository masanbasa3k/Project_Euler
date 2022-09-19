#Project euler problem 4
def checkPalindrome(x):
    number =  str(x)
    reverseNum = number[::-1]
    if number == reverseNum:
        return True
    else:
        return False

biggestPalindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        if checkPalindrome(i*j) and i*j > biggestPalindrome:
            biggestPalindrome = i*j
print(biggestPalindrome)