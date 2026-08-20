file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
new_lines = []
prevline = lines[0]
total = 0
target = "|"
s = "S"
for line in lines:
    indices=[index for index, value in enumerate(prevline) if value == target or value == s]
    for i in indices:
        if prevline[i] == "|":
            total += 1
            correct_line =""
            for x in range(len(prevline)):
                if x == i-1 or x == i+1:
                    correct_line += "|"
                elif x == i:
                    correct_line += "^"
                else:
                    correct_line += "."
            new_lines.append(correct_line)
        elif prevline[i] == "S":
            x = line.replace(line[i],"|")
            new_lines.append(line)
            new_lines.append(x)
            total+=1
        else:
            new_lines.append(line)
    prevline = new_lines[-1]

print(new_lines)
