file = open("adventofcode_secretentrance.txt", "r")

def get_adjacent(field, row, col):
    rows, cols = len(field), len(field[0])
    adjacent = []
    for r in range(max(0,rows-1),min(rows,rows+2)):
        for c in range(max(0,cols-1),min(cols,cols+2)):
            if(r,c) != (row,col):
                adjacent.append(adjacent[r][c])
field = []
for l in file:
    row = list(l)
    if "/n" in row:
        row.pop()
    field.append(row)


print(field)