import math

ans = []
resultNumerator = 1
resultDenominator = 1

for i in range(10, 100):
    for j in range(i + 1, 100):
        if i % 10 == 0:
            continue
        if j % 10 == 0:
            continue

        stri = str(i)
        strj = str(j)

        if stri[1] == strj[0] and int(stri[0]) / int(strj[1]) == i / j:
            ans.append(str(i) + '/' + str(j))
            resultNumerator *= i
            resultDenominator *= j
        if stri[0] == strj[1] and int(stri[1]) / int(strj[0]) == i / j:
            ans.append(str(i) + '/' + str(j))
            resultNumerator *= i
            resultDenominator *= j
        if stri[1] == strj[1] and int(stri[0]) / int(strj[0]) == i / j:
            ans.append(str(i) + '/' + str(j))
            resultNumerator *= i
            resultDenominator *= j
        if stri[0] == strj[0] and int(stri[1]) / int(strj[1]) == i / j:
            ans.append(str(i) + '/' + str(j))
            resultNumerator *= i
            resultDenominator *= j

print(resultDenominator // math.gcd(resultDenominator, resultNumerator))