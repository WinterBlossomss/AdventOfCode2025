file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
coordinates = []
max_area = 0

for line in lines:
    num1,num2 = line.split(",")
    coordinates.append([int(num1),int(num2)])

for i in range(len(coordinates)):
    for j in range(i+1,len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]

        # Calculate differences(+1 to include perimeter)
        width = abs(x2 - x1)+1
        height = abs(y2 - y1)+1
        area = width * height

        # Update maximum area found
        if area > max_area:
            max_area = area
            best_pair = (coordinates[i], coordinates[j])


print(max_area)
