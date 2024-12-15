import collections
import sys

file_path = sys.argv[1]
file = open(file_path).read()

g, m = file.split("\n\n")

expansion = {
    "#" : "##",
    "O" : "[]",
    "." : "..",
    "@" : "@."
}

directions = {
    "^" : (-1, 0),
    "v" : (1, 0),
    "<" : (0, -1),
    ">" : (0, 1)
}

grid = [[y for y in x] for x in g.split("\n")]
new_grid = [[elem for y in x for elem in expansion[y]] for x in grid]
movements = "".join(m.split("\n"))


M, N = len(grid), len(grid[0])


pos = [-1, -1]


for r in range(M) :
    for c in range(N) :
        if grid[r][c] == "@" :
            pos = [r, c]


for m in movements :
    r, c = pos
    dr, dc = directions[m]

    rr, cc = r + dr, c + dc

    if grid[rr][cc] == "#" :
        continue
    elif grid[rr][cc] == "O" :
        while grid[rr][cc] == "O" :
            rr, cc = rr + dr, cc + dc

        if grid[rr][cc] == "." :
            ar, ac = -dr, -dc 
            while (rr, cc) != (r + dr, c + dc) :
                grid[rr][cc] = "O"
                rr, cc  = rr + ar, cc + ac
            grid[rr][cc] = "@"
            grid[r][c] = "."
            pos = [rr, cc]
    else :
        pos = [rr, cc]
        grid[r][c] = "."
        grid[rr][cc] = "@"

part_one = 0

for r in range(M) :
    for c in range(N) :
        if grid[r][c] == "O" :
            part_one += 100 * r + c

print(f"part one asnwer is {part_one}")

grid = new_grid
M, N = len(grid), len(grid[0])

for r in range(M) :
    for c in range(N) :
        if grid[r][c] == "@" :
            pos = [r, c]




def get_box_boundaries(pos, grid):
    r, c = pos

    return [[r, c], [r, c + 1]] if grid[r][c] == "[" else [[r, c - 1], [r, c]]

def skip_box(pos, direction) :
    r, c = pos
    dr, dc = direction

    return [r + dr + dr, c + dc + dc]

def get_box_stack(start, direction, grid) :
    stack = []
    boxes_to_process = collections.deque()
    boxes_to_process.append(start)
    dr, dc = direction

    while boxes_to_process :
        layer = []
        for _ in range(len(boxes_to_process)) :
            box = boxes_to_process.popleft()

            for er, ec in box :
                if grid[er + dr][ec + dc] == "#" :
                    return "#"
                if grid[er + dr][ec + dc] in "[]" :
                    boxes_to_process.append(get_box_boundaries([er + dr, ec + dc], grid))

            layer.append(box)

        stack.append(layer)

    return stack

def move_boxes(boxes, direction, grid) :
    grid_copy = [[y for y in x]for x in grid]
    dr, dc = direction

    for b in reversed(boxes)  :
        for er, ec in b :
            grid_copy[er + dr][ec + dc] = grid[er][ec]
            grid_copy[er][ec] = "."

    return grid_copy



for m in movements :
    r, c = pos
    dr, dc = directions[m]

    rr, cc = r + dr, c + dc

    if grid[rr][cc] == "#" :
        continue
    elif grid[rr][cc] == "." :
        grid[r][c] = "."
        grid[rr][cc] = "@"
        pos = [rr, cc]
    else :
        box = get_box_boundaries([rr, cc], grid)
        boxes = [box]
        if m in ["<", ">"] : 
            rr, cc = skip_box([rr, cc], [dr, dc])

            while grid[rr][cc] in ["[", "]"] :
                boxes.append(get_box_boundaries([rr, cc], grid))
                rr, cc = skip_box([rr, cc], [dr, dc])


            if grid[rr][cc] == "#" :
                continue

            ar, ac = -dr, -dc 

            while grid[rr][cc] != "@" :
                grid[rr][cc] = grid[rr + ar][cc + ac]
                rr, cc = rr + ar , cc + ac
        
            grid[r][c] = "."
            pos = [r + dr, c + dc]
        else :
            layer = get_box_stack(box, [dr, dc], grid)

            if layer != "#" :
                for boxes in reversed(layer) :
                    grid = move_boxes(boxes, [dr, dc], grid)
                grid[r][c] = "."
                grid[r + dr][c + dc] = "@"
                pos = [r + dr, c + dc]
                for er, ec in box :
                    if grid[er][ec] !=  "." :
                        grid[er][ec] = '@'



part_two = 0
for r in range(M) :
    for c in range(N) :
        if grid[r][c] == "[" :
            part_two += r * 100 + c

print(f"part two answer is {part_two}")
