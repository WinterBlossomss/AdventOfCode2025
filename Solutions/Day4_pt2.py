file = open("adventofcode_secretentrance.txt", "r")

def isValid(x, y, r, c):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True

def get_adjacent(arr, i, j):

    # Size of given 2d array
    r = len(arr)
    c = len(arr[0])

    rolls = []

    # directions
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for dx, dy in dirs:
        x, y = i + dx, j + dy
        if isValid(x, y, r, c):
            rolls.append(arr[x][y])


    return rolls


total = 0
temprollcount= 0
field = []
for l in file:
    row = list(l.rstrip("\n"))
    field.append(row)
while True:
    temprollcount = 0
    for r, row in enumerate(field):
        colnum = len(row)
        for col in range(colnum):
            elem = field[r][col]
            if elem == "@":
                adj = get_adjacent(field, r, col)
                count = adj.count("@")
                print("".join(map(str, adj)))
                if count < 4:
                    total += 1
                    temprollcount += 1
                    field[r][col] = "."
    if temprollcount == 0:
        break


print(total)