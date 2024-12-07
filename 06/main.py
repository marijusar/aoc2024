import sys
from typing import List

file_path = sys.argv[1]
file = open(file_path)
matrix = [[y for y in x.strip()] for x in file.readlines()]

M, N = len(matrix), len(matrix[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


part_one = 0
starting_position = [-1, -1]

for r in range(M) :
    for c in range(N) :
        if matrix[r][c] == "^" :
            starting_position = [r, c]
            break

def go():
        r, c = starting_position
        i = 0
        visited = set()
        loop_detector = set()
        while 0 <= r < M and 0 <= c <= N :
            visited.add((r ,c))
            while True :
                if (r, c ,i) in loop_detector :
                    return set()

                dr, dc = directions[i]
                rr, cc = r + dr, c + dc

                if 0 <= rr < M and 0 <= cc < N and matrix[rr][cc] == "#" :
                    i = (i + 1) % 4
                else :
                    break
            
            loop_detector.add((r, c, i))
            r, c = rr, cc

        return visited

path = go()
part_one = len(path)            
print(f"part one answer is {part_one}")


part_two = 0

for r, c in path :
    if matrix[r][c] == ".":
        matrix[r][c] = "#"

        if len(go()) == 0:
            part_two += 1

        matrix[r][c] = "."


print(f"part two answer is {part_two}")
