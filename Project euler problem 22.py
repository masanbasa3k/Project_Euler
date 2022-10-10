import string # alphabet

with open("p022_names.txt", "r") as f:
    names = f.read()

d = dict()
alphabet = string.ascii_uppercase
count = 1

for i in alphabet:
    d[i] = count
    count += 1

names = names.split(",")
list.sort(names)

index = 1
sum = 0

for name in names:
    s = 0
    name = name[1:len(name)-1]
    for letter in name:
        s += d[letter]
    sum += s * index
    index += 1
print(sum)