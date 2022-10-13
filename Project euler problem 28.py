matrix = []
for i in range(0, 1001):
    matrix.append([0]*1001)
direction = "right"
i = 500
j = 500
matrix[i][j] = 1
number = 2

while number < 1001*1001:
    while direction == "right" and j < 1000:
        matrix[i][j+1] = number
        number += 1
        j += 1
        if matrix[i+1][j] == 0:
            direction = "down"
            break
    
    while direction == "down":
        matrix[i+1][j] = number
        number += 1
        i += 1
        if matrix[i][j-1] == 0:
            direction = "left"
            break

    while direction == "left":
        matrix[i][j-1] = number
        number += 1
        j -= 1
        if matrix[i-1][j] == 0:
            direction = "up"
            break

    while direction == "up":
        matrix[i-1][j] = number
        number += 1
        i -= 1
        if matrix[i][j+1] == 0:
            direction = "right"
            break

sum = 0
for i in range(1001):
    sum += matrix[i][i]
    sum += matrix[1000-i][i]
sum -= matrix[500][500]
print(sum)