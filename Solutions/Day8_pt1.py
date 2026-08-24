import numpy as np
file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]

num_of_pairs = 1000
index1 = ""
index2 = ""
coords = []
distances = []

for line in lines:
    x,y,z = (int(x) for x in line.split(","))
    coords.append([x,y,z])

lencoords = len(coords)
circuits = [{x} for x in range(lencoords)] # used for "Union-Find"
for coord1 in range(lencoords):
    for coord2 in range(coord1 + 1, lencoords):
        x = (coords[coord1][0] - coords[coord2][0]) ** 2
        y = (coords[coord1][1] - coords[coord2][1]) ** 2
        z = (coords[coord1][2] - coords[coord2][2]) ** 2
        distances.append([x + y + z, [coord1, coord2]]) #saves "Euclidean distance", point 1 and point 2
#sort from largest distance to smallest distance
distances.sort(reverse=True)

while num_of_pairs>0:
    num_of_pairs -= 1
    coord1,coord2 = distances.pop()[1] # get the two coordinates

    index1 = index2 = None
    # finds circuit it belongs to
    for i, circuit in enumerate(circuits):
        if coord1 in circuit:
            index1 = i
        if coord2 in circuit:
            index2 = i

    if index1 != index2:
        lo, hi = min(index1, index2), max(index1, index2)
        circuits[lo] = circuits[lo] | circuits[hi] #merge the sets, write into the lower index
        del circuits[hi] #delete higher index

circuits.sort(key=lambda c: len(c))
total = len(circuits.pop()) * len(circuits.pop()) * len(circuits.pop())
print(total)