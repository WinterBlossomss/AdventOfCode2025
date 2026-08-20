file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
start = lines[0].index('S')
hits = {start:1}

for line in lines:
    new_hits = {}
    for index,count in hits.items():
        if line[index] == "^":
            new_hits[index-1] = new_hits.get(index-1,0)+count
            new_hits[index+1] = new_hits.get(index+1,0)+count
        else:
            new_hits[index] = new_hits.get(index,0)+count
        hits = new_hits


print(sum(hits.values()))
