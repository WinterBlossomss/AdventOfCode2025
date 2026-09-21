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

ranges.sort()
mergedranges = []

for start, end in ranges:
    # compare start with current range end - merge (take start and end to make new range)
    if mergedranges and start <= mergedranges [-1][1] + 1:
        mergedranges[-1] = (mergedranges[-1][0], max(mergedranges[-1][1], end))
    else:
        mergedranges.append((start, end))
    total = sum(end - start + 1 for start, end in mergedranges)

print(total)
# print(ranges)
# print(ids)
