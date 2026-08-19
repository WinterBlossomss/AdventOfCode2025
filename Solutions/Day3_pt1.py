file = open("adventofcode_secretentrance.txt", "r")

total = 0

def getbattery(num):
    s = str(num)
    n = len(s)
    for d in range(1, n):
        if n % d == 0 and s[:d] * (n // d) == s:
            return True
    return False

numList = file.readlines()
for l in numList:
    bank = list(l)
    sortmax2=0
    jolt = 0
    x = 0
    max1 = 0
    max2 = 0
    pos1 = 0
    pos2 = 0
    max2,max1 = sorted(bank)[-2:]
    pos1 = bank.index(max1)
    pos2 = bank.index(max2)
    # if higher number is first ( 9 1 )
    if (pos1 < pos2):
        jolt = int(str(max1)+str(max2))
    #if higher number is second ( 1 9 )
    else:
        x = l[pos1:]
        x = x[1:]
        if x != '\n':
            sortmax2 = sorted(x)[-1]
            jolt = int(str(max1) + str(sortmax2))
        else:
            jolt = int(str(max2) + str(max1))


    total += jolt
    print("bank = " + l)
    print("x = " + str(x))
    print("max1 = " + max1)
    print("max2 = " + str(max2))
    print("sortmax2 = " + str(sortmax2))
    print("pos1 = " + str(pos1))
    print("pos2 = " + str(pos2))
    print("jolt = " + str(jolt))
    print("total = " + str(total))
    print("------------------")

print(total)