points = 0
startPos=50
maxPos=99
minPos=0

print("startPos:", startPos)
print("maxPos:", maxPos)
file = open("adventofcode_secretentrance.txt", "r")
for l in file:
    print("Start Position:" + str(startPos))
    direction = l[0]
    print("direction: " + direction)
    count = l[1:]
    print("count: " + count)

    num = int(count)
    if direction == "L":
        for i in range(num):
            startPos = startPos - 1
            if startPos == -1:
                startPos = maxPos
    else:
        for i in range(num):
            startPos = startPos + 1
            if startPos == 100:
                startPos = minPos
    if startPos == 0:
        print("Zero here")
        points += 1

print("Points:", points)