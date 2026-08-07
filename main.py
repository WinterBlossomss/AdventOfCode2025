file = open("adventofcode_secretentrance.txt", "r")

total = 0

numList = file.readlines()
for l in numList:
    print (l)
    idList = l.split(",")
    print (idList)
    for id in idList:
        individ = id.split("-")
        print (individ)
        num1 = int(individ[0])
        num2 = int(individ[1])
        counter = num1 -1
        idRange = num2 - num1
        print (idRange)
        for i in range(idRange):
            counter += 1
            count = len(str(counter))
            if count % 2 != 0:
                temp = list(map(int, str(counter)))
                num = len(str(temp[0]))
                # compare all list items
                for i in range(num):
                    for j in range(i + 1, num):
                        compare(temp[i], temp[j])
            else:
                temp = str(counter)
                q, r = divmod(len(temp), 2)
                part1, part2 = temp[:q + r], temp[q + r:]
                if part1 == part2:
                    total += int(counter)

print (total)

def compare(num1, num2):
    if num1 == num2:
