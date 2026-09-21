from fractions import Fraction
file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
file.close() # forgot to add this in prev examples ;-;

total = 0
lights = []
buttons = []
joltages = []

for line in lines:
    button = []


    # Parse buttons as lists of ints
    x = line.split("] ")[1].split(" {")[0]
    x = x.split(" ")
    for b in x:
        temp = b.split("(")[1].split(")")[0]
        button.append([int(v) for v in temp.split(",")])
    buttons.append(button)

    x = line.split("{")[1].split("}")[0]
    joltage = [int(v) for v in x.split(",")]
    joltages.append(joltage)


def _pivot(tableau, basis, obj_row_index, num_cols):
    num_rows = len(tableau)

    while True:
        obj = tableau[obj_row_index]

        pivot_col = None
        for j in range(num_cols):
            if obj[j] < 0:
                pivot_col = j
                break
        if pivot_col is None:
            return

        pivot_row = None
        best_ratio = None
        for i in range(num_rows):
            if i == obj_row_index:
                continue
            entry = tableau[i][pivot_col]
            if entry > 0:
                ratio = tableau[i][-1] / entry
                if (best_ratio is None or ratio < best_ratio or
                        (ratio == best_ratio and basis[i] < basis[pivot_row])):
                    best_ratio = ratio
                    pivot_row = i

        pivot_val = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [v / pivot_val for v in tableau[pivot_row]]
        for i in range(num_rows):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                if factor != 0:
                    tableau[i] = [tableau[i][k] - factor * tableau[pivot_row][k]
                                  for k in range(len(tableau[i]))]
        basis[pivot_row] = pivot_col
def solve_lp_min_sum(rows, num_vars, cost):
    m = len(rows)

    norm_rows = []
    for coeffs, rhs in rows:
        if rhs < 0:
            coeffs = [-c for c in coeffs]
            rhs = -rhs
        norm_rows.append((coeffs, rhs))

    num_cols_p1 = num_vars + m
    tableau = []
    for i, (coeffs, rhs) in enumerate(norm_rows):
        row = [Fraction(c) for c in coeffs]
        row += [Fraction(1) if k == i else Fraction(0) for k in range(m)]
        row.append(Fraction(rhs))
        tableau.append(row)

    basis = [num_vars + i for i in range(m)]

    obj_row = []
    for j in range(num_vars):
        obj_row.append(-sum(tableau[i][j] for i in range(m)))
    obj_row += [Fraction(0)] * m
    obj_row.append(-sum(tableau[i][-1] for i in range(m)))
    tableau.append(obj_row)
    obj_row_index = m

    _pivot(tableau, basis, obj_row_index, num_cols_p1)

    if -tableau[obj_row_index][-1] != 0:
        return None

    for i in range(m):
        if basis[i] >= num_vars:
            for j in range(num_vars):
                if tableau[i][j] != 0:
                    pivot_val = tableau[i][j]
                    tableau[i] = [v / pivot_val for v in tableau[i]]
                    for r in range(len(tableau)):
                        if r != i:
                            factor = tableau[r][j]
                            if factor != 0:
                                tableau[r] = [tableau[r][k] - factor * tableau[i][k]
                                              for k in range(len(tableau[r]))]
                    basis[i] = j
                    break

    new_tableau = [r[:num_vars] + [r[-1]] for r in tableau[:m]]

    obj_row2 = []
    for j in range(num_vars):
        reduced = Fraction(cost[j])
        for i in range(m):
            bi = basis[i]
            if bi < num_vars and cost[bi] != 0:
                reduced -= Fraction(cost[bi]) * new_tableau[i][j]
        obj_row2.append(reduced)
    obj_val = Fraction(0)
    for i in range(m):
        bi = basis[i]
        if bi < num_vars and cost[bi] != 0:
            obj_val -= Fraction(cost[bi]) * new_tableau[i][-1]
    obj_row2.append(obj_val)
    new_tableau.append(obj_row2)

    _pivot(new_tableau, basis, m, num_vars)

    x = [Fraction(0)] * num_vars
    for i in range(m):
        if basis[i] < num_vars:
            x[basis[i]] = new_tableau[i][-1]
    return x
def ilp_min_sum(buttons, joltages):
    n = len(buttons)      # number of buttons for this machine
    m = len(joltages)     # number of counters for this machine

    # Base equality constraints: for each counter j, the sum of presses
    # of every button that touches counter j must equal joltages[j]
    base_rows = []
    for j in range(m):
        coeffs = [1 if j in buttons[i] else 0 for i in range(n)]
        base_rows.append((coeffs, joltages[j]))

    best = {"obj": None, "x": None}  # tracks the best whole-number solution found

    def recurse(extra_rows, num_extra_vars):
        num_vars = n + num_extra_vars
        rows = []
        for coeffs, rhs in base_rows:
            rows.append((coeffs + [0] * num_extra_vars, rhs))
        rows.extend(extra_rows)

        cost = [1] * n + [0] * num_extra_vars  # minimize total real button presses only

        x = solve_lp_min_sum(rows, num_vars, cost)
        if x is None:
            return  # this branch has no feasible solution at all -- dead end

        lp_obj = sum(x[:n])
        if best["obj"] is not None and lp_obj >= best["obj"]:
            return  # even the best case here can't beat what we already have -- prune

        # Look for a button whose press-count came out fractional
        frac_i = None
        frac_val = None
        for i in range(n):
            if x[i].denominator != 1:
                frac_i = i
                frac_val = x[i]
                break

        if frac_i is None:

            total = sum(x[:n])
            if best["obj"] is None or total < best["obj"]:
                best["obj"] = total
                best["x"] = [int(v) for v in x[:n]]
            return

        floor_val = frac_val.numerator // frac_val.denominator
        ceil_val = floor_val + 1

        padded_extra_rows = [(coeffs + [0], rhs) for coeffs, rhs in extra_rows]

        le_coeffs = [0] * n + [0] * num_extra_vars + [1]
        le_coeffs[frac_i] = 1
        recurse(padded_extra_rows + [(le_coeffs, floor_val)], num_extra_vars + 1)

        ge_coeffs = [0] * n + [0] * num_extra_vars + [-1]
        ge_coeffs[frac_i] = 1
        recurse(padded_extra_rows + [(ge_coeffs, ceil_val)], num_extra_vars + 1)

    recurse([], 0)

    return best["obj"]
def solve(buttons, joltages):
    total = 0
    for button_list, target in zip(buttons, joltages):
        total += ilp_min_sum(button_list, target)
    return total


x = solve(buttons, joltages)
print(x)