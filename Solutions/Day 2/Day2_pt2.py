file = open("adventofcode_secretentrance.txt", "r")

total = 0

def compare(num):
    s = str(num)
    n = len(s)
    for d in range(1, n):
        # n = total length of string
        # d = block length (section you are checking for repeats)
        # first check: does the block length divide evenly into total length
        # second check: does repeating the block d*(n//d) times reproduce the original
        if n % d == 0 and s[:d] * (n // d) == s:
            return True
    return False


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
        idRange = num2 - num1 + 1
        print (idRange)
        for i in range(idRange):
            counter += 1
            if compare(counter):
                total += counter

print (total)
