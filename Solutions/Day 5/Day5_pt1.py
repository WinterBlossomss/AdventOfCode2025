file = open("adventofcode_secretentrance.txt", "r")

total = 0
ranges = []
ids = []

for row in file:
    row = row.strip()
    if not row: # skip stinky empty line dumb dumb empy line
        continue
    if "-" in row:
        start, end = map(int, row.split("-"))
        ranges.append((start, end))
    else:
        ids.append(int(row))

in_range = [id for id in ids if any(start <= id <= end for start, end in ranges)]
total = len(in_range)

print(total)
# print(ranges)
# print(ids)
