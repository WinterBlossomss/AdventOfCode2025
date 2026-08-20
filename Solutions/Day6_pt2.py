file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
total = 0
calculations = []

def combine(op, nums):
    if op == "+":
        return sum(nums) # addition sum
    total = 1
    for n in nums:
        total *= n
    return total

*rows, op_row = lines
width = max(len(r) for r in lines)
rows = [r.ljust(width) for r in rows]
op_row = op_row.ljust(width)

columns = list(zip(*rows, op_row))

#"*" unpacks list into individual elements
for *digits, op in columns:
    if op in "+*":
        calculations.append({"op": op, "cols": []})
    calculations[-1]["cols"].append("".join(digits).replace(" ", ""))

for calc in calculations:
    operands = [int(c) for c in reversed(calc["cols"]) if c]
    if calc["op"] == "+":
        temp = sum(operands)
    else:
        temp = 1
        for n in operands:
            temp *= n
    total += temp
print(total)
