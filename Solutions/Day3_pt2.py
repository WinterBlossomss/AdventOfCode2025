file = open("adventofcode_secretentrance.txt", "r")
total = 0
numList = file.readlines()
for l in numList:
    bank = l.strip()

    removalcount = len(bank) - 12 # number of digits
    stack = [] # highest number goes here by the digit
    for digit in bank:
        # checks if previous number is bigger than digit
        # pop previously added digit if smaller than current digit (until no removals left) and append digit regardless
        while stack and removalcount > 0 and stack[-1] < digit:
            stack.pop()
            removalcount -= 1

        stack.append(digit)

    jolt = int("".join(stack[:12]))
    total += jolt

print(total)




