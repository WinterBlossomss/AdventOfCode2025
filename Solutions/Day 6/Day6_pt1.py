file = open("adventofcode_secretentrance.txt", "r")

total = 0
calculations = []
numrowcount=4

columns = list(zip(*[line.split() for line in file]))

for calc in columns:
    temp = 0
    if calc[numrowcount] == '+':
        for num in range(0,numrowcount):
            temp += int(calc[num])
    elif calc[numrowcount] == '*':
        temp = 1
        for num in range(0,numrowcount):
            temp *= int(calc[num])
    total += temp

print(total)
