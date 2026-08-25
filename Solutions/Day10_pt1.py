def n_length_combo(lst, n):
    # Base case: there's exactly one way to choose 0 elements —
    # the empty combination. This also stops the recursion
    if n == 0:
        return [[]]

    l = []  # will hold every combination of length n found

    # Try each element in turn as the "first" element of a combination
    for i in range(0, len(lst)):
        m = lst[i]  # the element to include this "run"

        # Only elements after index i are eligible partners for m
        # Excluding everything before/at i guarantees each combination
        # is built in a consistent order and is never produced twice
        remLst = lst[i + 1:]

        # Recursively find all ways to fill the remaining (n-1) slots
        # using only elements from remLst
        remainlst_combo = n_length_combo(remLst, n - 1)

        # Combine m with each of those smaller combinations to form
        # a full combination of length n
        for p in remainlst_combo:
            l.append([m, *p])

    return l # returns each combination of length n found


file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
file.close() # forgot to add this in prev examples ;-;

total = 0
lights = []
buttons = []
joltages = []

for line in lines:
    button = []

    # Parse lights as booleans
    x = line.split("[")[1].split("]")[0]
    light_row = [c == "#" for c in x]
    lights.append(light_row)

    # Parse buttons as lists of ints
    x = line.split("] ")[1].split(" {")[0]
    x = x.split(" ")
    for b in x:
        temp = b.split("(")[1].split(")")[0]
        temp2 = temp.split(",")
        button.append([int(v) for v in temp2])
    buttons.append(button)

    # Unnecessary for this part
    x = line.split("{")[1].split("}")[0]
    x = x.split(",")
    joltages.append(x)


def min_presses_for_machine(target, button_list):
    num_lights = len(target)
    num_buttons = len(button_list)
    button_indices = list(range(num_buttons))

    # tries using 0 buttons, then 1 button, then 2 buttons, etc.
    # Because it checks smaller sizes first, the first match it finds is guaranteed to be the minimum number of presses
    for r in range(0, num_buttons + 1):
        combos = n_length_combo(button_indices, r)  # all ways to choose r buttons
        for combo in combos:
            # Start with all lights off
            state = [False] * num_lights

            # Simulate pressing every button in this combination once
            for bidx in combo:
                for pos in button_list[bidx]:
                    state[pos] = not state[pos]  # toggle that light

            # If this combination produces exactly the target pattern,
            # we've found a valid solution using r presses
            if state == target:
                return r
    # this shouldn't hit unless there ain't a solution
    return False

# zip to use two vars from each array for the method
for target, button_list in zip(lights, buttons):
    presses = min_presses_for_machine(target, button_list)
    total += presses

print(total)