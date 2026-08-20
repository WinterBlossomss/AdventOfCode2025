file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
total = 0
start = lines[0].index('S')
hits = [start]

for line in lines:
    new_hits = []
    for index in hits:
        if line[index] == "^":
            total += 1
            left = index-1
            right = index+1
            if left not in new_hits:
                new_hits.append(left)
            if right not in new_hits:
                new_hits.append(right)
        else:
            if index not in new_hits:
                new_hits.append(index)
        hits = new_hits


print(total)
