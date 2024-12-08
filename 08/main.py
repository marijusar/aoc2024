import sys
from collections import defaultdict

file_path = sys.argv[1]
file = open(file_path)

grid = [[y for y in x.strip()] for x in file.readlines()]
M, N = len(grid), len(grid[0])

antennas = defaultdict(list)
antennas_set = set()

for r in range(M) :
    for c in range(N) : 
        if grid[r][c] != "." :
            antennas[grid[r][c]].append([r, c])
            antennas_set.add((r, c))

part_one = 0

antinodes = set()


for antenna in antennas :
    k = len(antennas[antenna])
    for i in range(k) :
        for j in range(i + 1, k) :
            x1, y1 = antennas[antenna][i]
            x2, y2 = antennas[antenna][j]

            x3, y3 = 2 * x1 - x2, 2 * y1 - y2
            x4, y4 = 2 * x2 - x1, 2 * y2 - y1

            antinodes.add((x3, y3))
            antinodes.add((x4, y4))



for x, y in antinodes :
    if 0 <= x < M and 0 <= y < N :
        part_one += 1


print(f"part one answer is {part_one}")

antinodes = set()

for antenna in antennas :
    k = len(antennas[antenna])
    for i in range(k) :
        for j in range(i + 1, k) :
            x1, y1 = antennas[antenna][i]
            x2, y2 = antennas[antenna][j]

            x1_t, y1_t = x1, y1
            x2_t, y2_t = x2, y2

            while 0 <= x1_t < M and 0 <= y1_t < N :
                x3, y3 = 2 * x1_t - x2_t, 2 * y1_t - y2_t

                x2_t, y2_t = x1_t, y1_t
                x1_t, y1_t = x3, y3

                antinodes.add((x3, y3))


            x1_t, y1_t = x1, y1
            x2_t, y2_t = x2, y2

            while 0 <= x2_t < M and 0 <= y2_t < N :
                x4, y4 = 2 * x2_t - x1_t, 2 * y2_t - y1_t

                x1_t, y1_t = x2_t, y2_t
                x2_t, y2_t = x4, y4

                antinodes.add((x4, y4))


part_two = len(antennas_set)

for x, y in antinodes :
    if 0 <= x < M and 0 <= y < N and (x , y) not in antennas_set:
        grid[x][y] = "#"
        part_two += 1

[print("".join(x)) for x in grid]

print(f"part two answer is {part_two}")

# [[0, 6], [0, 11], [1, 3], [2, 4], [2, 10], [3, 2], [4, 9], [5, 1], [6, 3], [7, 0], [7, 7], [10, 10], [11, 10]]

