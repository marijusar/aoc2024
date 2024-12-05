import collections
import sys

file_path = sys.argv[1]
file = open(file_path)

matrix = [[y for y in x.strip()] for x in file.readlines()]

q = collections.deque()

characters = ["X", "M", "A", "S"]

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
]


starting_positions = []

for r in range(len(matrix)) :
    for c in range(len(matrix[0])) :
        if matrix[r][c] == "X" :
            for direction in directions :
                starting_positions.append([[r, c], direction])


for p in starting_positions :
    q.append(p)

part_one = 0

while q :
    p, d = q.popleft()
    r , c = p
    dr, dc = d
    current_idx = characters.index(matrix[r][c])
    if matrix[r][c] == characters[-1] :
        part_one += 1
    else :
        rr, cc = r + dr, c + dc 

        if (
            rr < 0 or
            cc < 0 or
            rr == len(matrix) or
            cc == len(matrix[0]) or
            matrix[rr][cc] != characters[current_idx + 1]
        ) :
            continue

        q.append([[rr, cc], d])


print(f"part one answer is : {part_one}")

part_two = 0

coordinate_pairs = [
    [(-1, -1), (1, 1)],
    [(-1, 1), (1, -1)]
]

def is_valid_layout(coords) :
    r, c = coords
    combos = 0

    for pair in coordinate_pairs :
        acc = []
        for dr, dc in pair : 
            rr, cc = r + dr, c + dc
            if (
                rr < 0 or 
                rr == len(matrix) or
                cc < 0 or 
                cc == len(matrix[0]) 
                ) :
                return False

            acc.append(matrix[rr][cc])

        acc.sort()

        if acc == ["M", "S"] :
            combos += 1

    return combos == 2

for r in range(len(matrix)) :
    for c in range(len(matrix[0])) :
        if matrix[r][c] == "A" and is_valid_layout([r, c]) :
            part_two += 1


print(f"part two answer is : {part_two}")

