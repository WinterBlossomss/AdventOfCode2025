file = open("adventofcode_secretentrance.txt", "r")
lines = [line.rstrip("\n") for line in file]

def is_point_inside_polygon(point_x, point_y, coordinates):
    is_inside = False
    count_tiles = len(coordinates)
    # look through every edge of the polygon
    for i in range(count_tiles):
        edge_start_x, edge_start_y = coordinates[i]
        edge_end_x, edge_end_y = coordinates[(i + 1) % count_tiles]
        if (edge_start_y > point_y) != (edge_end_y > point_y): # edge crosses this height? (skips horizontal edges automatically)
            crossing_x = edge_start_x + (point_y - edge_start_y) / (edge_end_y - edge_start_y) * (edge_end_x - edge_start_x) # where does it cross horizontally, saves x coord
            if point_x < crossing_x: # ray only goes to right,
                is_inside = not is_inside
    return is_inside


def edge_cuts_into_rectangle(edge, rect_left, rect_right, rect_bottom, rect_top):
    (start_x, start_y), (end_x, end_y) = edge

    if start_x == end_x:  # vertical edge
        edge_x = start_x
        edge_bottom, edge_top = sorted((start_y, end_y))
        if rect_left < edge_x < rect_right and max(edge_bottom, rect_bottom) < min(edge_top, rect_top):
            return True
    else:  # horizontal edge
        edge_y = start_y
        edge_left, edge_right = sorted((start_x, end_x))
        if rect_bottom < edge_y < rect_top and max(edge_left, rect_left) < min(edge_right, rect_right):
            return True

    return False


def rectangle_is_fully_inside(coordinates, polygon_edges, corner_a, corner_b):
    corner_a_x, corner_a_y = corner_a
    corner_b_x, corner_b_y = corner_b

    rect_left, rect_right = sorted((corner_a_x, corner_b_x))  # smaller x = left, bigger x = right
    rect_bottom, rect_top = sorted((corner_a_y, corner_b_y))  # smaller y = bottom, bigger y = top


    if rect_left == rect_right or rect_bottom == rect_top:
        return False

    # a point guaranteed to be inside the candidate rectangle
    sample_x = rect_left + 0.5
    sample_y = rect_bottom + 0.5
    if not is_point_inside_polygon(sample_x, sample_y, coordinates):
        return False

    for edge in polygon_edges:
        if edge_cuts_into_rectangle(edge, rect_left, rect_right, rect_bottom, rect_top):
            return False

    return True

coordinates = []
candidate_rectangles = []

for line in lines:
    x_str, y_str = line.split(",")
    coordinates.append((int(x_str), int(y_str)))

num_tiles = len(coordinates)
polygon_edges = [(coordinates[i], coordinates[(i + 1) % num_tiles]) for i in range(num_tiles)]

# build every possible rectangle and sort biggest-area-first
for i in range(num_tiles):
    for j in range(i + 1, num_tiles):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]

        # Calculate differences(+1 to include perimeter)
        width = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        candidate_rectangles.append((area, [x1,y1], [x2,y2]))

candidate_rectangles.sort(key=lambda rectangle: -rectangle[0])

# test rectangles largest first, stop at the first valid one (largest possible)
for area, coord_a, coord_b in candidate_rectangles:
    if rectangle_is_fully_inside(coordinates, polygon_edges, coord_a, coord_b):
        print(area)
        break