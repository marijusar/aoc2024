import sys

file_path = sys.argv[1]
file = open(file_path)

grid = [[int(y) for y in x.strip()] for x in file.readlines()]
M, N = len(grid), len(grid[0])


directions = [(1, 0,), (0, 1), (-1, 0), (0, -1)]

def dfs_one(p, seen) :
    r, c = p
    if grid[r][c] == 9  :
        seen.add(p)
        return seen

    for dr, dc in directions :
        rr, cc = r + dr, c + dc

        if (
            rr < 0 or
            cc < 0 or 
            rr == M or
            cc == N or
            grid[rr][cc] != grid[r][c] + 1
            ) :
            continue

        dfs_one((rr , cc), seen)

    return seen


part_one = 0

    
for r in range(M) :
    for c in range(N) :
        if grid[r][c] == 0 :
            a = dfs_one((r, c), set())
            part_one += len(a)

print(f"part one answer is {part_one}")
        
def dfs_two(p) :
    r, c = p
    if grid[r][c] == 9  :
        return 1

    ans = 0

    for dr, dc in directions :
        rr, cc = r + dr, c + dc

        if (
            rr < 0 or
            cc < 0 or 
            rr == M or
            cc == N or
            grid[rr][cc] != grid[r][c] + 1
            ) :
            continue

        ans += dfs_two((rr , cc))


    return ans

part_two = 0

for r in range(M) :
    for c in range(N) :
        if grid[r][c] == 0 :
            part_two += dfs_two((r, c))


print(f"part two answer is {part_two}")

