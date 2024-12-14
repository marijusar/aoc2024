import sys
import re
from functools import reduce
from operator import mul
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

re_d = r"-?\d+"

file_path = sys.argv[1]
file = open(file_path)

config = {
    "input.txt" : [101, 103],
    "test.txt" : [11, 7],
}

M, N = config[file_path]

robots = [[int(y) for y in re.findall(re_d, x)] for x in file.readlines()]

part_one = [0, 0, 0, 0]

def get_quadrant(x, y) :
    m, n = M // 2, N // 2
    if x == m or y == n :
        return -1
    if x < m and y < n :
        return 0
    elif x > m and y < n :
        return 1
    elif x < m and y > n :
        return 2
    else :
        return 3


def get_next_coord(pos, v, limit, offset) :
    offset = v * offset
    if offset > 0 :
        return (pos + offset) % limit
    else :
        o = abs(offset) % limit

        if pos - o < 0 :
            return limit - abs(pos - o)
        else :
            return pos - o



grid = [["0"] * M for _ in range(N)]

for robot in robots :
    x, y, vx, vy = robot

    x = get_next_coord(x, vx, M, 100)
    y = get_next_coord(y, vy, N, 100)

    grid[y][x] = str(int(grid[y][x]) + 1)
 
    if get_quadrant(x, y) >= 0:
        part_one[get_quadrant(x, y)] += 1


grid = [["." if y == "0" else y for y in x] for x in grid]


part_one = reduce(mul, part_one)

print(f"part one answer is {part_one}")

frames = []
fig = plt.figure()
cache = set()

# observed clumping pattern for every 101 frame starting from frame 33
for i in range(33, 10404, 101) :
    grid = [["0"] * M for _ in range(N)]
    
    coords = []

    for robot in robots :
        x, y, vx, vy = robot

        x = get_next_coord(x, vx, M, i)
        y = get_next_coord(y, vy, N, i)

        grid[y][x] = str(int(grid[y][x]) + 1)
        coords.append((x, y))
    plt.xlabel(f"{i}")
    plt.imshow([[int(y) for y in x] for x in grid], animated=True)
    plt.savefig(f'{i}.png')
    

