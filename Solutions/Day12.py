file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]
file.close()

# split the lines into shape blocks and the region block
blocks = []
current_block = []
for line in lines:
    if line.strip() == "":
        if current_block:
            blocks.append(current_block)
            current_block = []
    else:
        current_block.append(line)
if current_block:
    blocks.append(current_block)

shape_blocks = blocks[:-1]
region_lines = blocks[-1]

# parse shapes
def parse_shape_grid(grid_lines):
    cells = []
    for r, line in enumerate(grid_lines):
        for c, ch in enumerate(line):
            if ch == '#':
                cells.append((r, c))
    return cells

def normalize(cells):
    min_r = min(r for r, c in cells)
    min_c = min(c for r, c in cells)
    return frozenset((r - min_r, c - min_c) for r, c in cells)

def all_orientations(cells):
    orientations = set()
    for flip in range(2):
        pts = [(r, -c) for r, c in cells] if flip else cells
        for rot in range(4):
            rotated = pts
            for _ in range(rot):
                rotated = [(c, -r) for r, c in rotated]
            orientations.add(normalize(rotated))
    return [sorted(o) for o in orientations]

shapes = {}
for block in shape_blocks:
    header = block[0]
    idx = int(header.split(":")[0])
    grid_lines = block[1:]
    cells = parse_shape_grid(grid_lines)
    shapes[idx] = all_orientations(cells)

# parse regions
regions = []
for line in region_lines:
    dims, counts_str = line.split(":")
    w, h = map(int, dims.strip().split("x"))
    counts = list(map(int, counts_str.strip().split()))
    regions.append((w, h, counts))

# backtracking placement solver
def can_fit(shapes, counts, W, H):
    shape_area = {sid: len(shapes[sid][0]) for sid in shapes}
    total_needed = sum(counts[sid] * shape_area.get(sid, 0) for sid in range(len(counts)))
    if total_needed > W * H:
        return False

    pieces_order = []
    for shape_id, cnt in enumerate(counts):
        pieces_order += [shape_id] * cnt
    if not pieces_order:
        return True

    grid = [[False] * W for _ in range(H)]
    empty_count = [W * H]

    areas = [shape_area[s] for s in pieces_order]
    suffix_area = [0] * (len(areas) + 1)
    for i in range(len(areas) - 1, -1, -1):
        suffix_area[i] = suffix_area[i + 1] + areas[i]

    def place(idx, last_pos):
        if idx == len(pieces_order):
            return True
        if suffix_area[idx] > empty_count[0]:
            return False

        shape_id = pieces_order[idx]
        orientations = shapes[shape_id]
        same_as_prev = idx > 0 and pieces_order[idx - 1] == shape_id
        start_o, start_r, start_c = last_pos if same_as_prev else (0, 0, 0)

        for o_idx in range(start_o, len(orientations)):
            cells = orientations[o_idx]
            max_r = max(r for r, c in cells)
            max_c = max(c for r, c in cells)
            r_lo = start_r if o_idx == start_o else 0
            for r in range(r_lo, H - max_r):
                c_lo = start_c if (o_idx == start_o and r == start_r) else 0
                for c in range(c_lo, W - max_c):
                    if any(grid[r + dr][c + dc] for dr, dc in cells):
                        continue
                    for dr, dc in cells:
                        grid[r + dr][c + dc] = True
                    empty_count[0] -= len(cells)
                    if place(idx + 1, (o_idx, r, c)):
                        return True
                    for dr, dc in cells:
                        grid[r + dr][c + dc] = False
                    empty_count[0] += len(cells)
        return False

    return place(0, (0, 0, 0))

# run over all regions
total = 0
for (w, h, counts) in regions:
    if can_fit(shapes, counts, w, h):
        total += 1

print(total)