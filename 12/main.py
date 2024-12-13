import sys
import collections

file_path = sys.argv[1]
file = open(file_path)

grid = [x.strip() for x in file.readlines()]

seen = set()

M, N = len(grid), len(grid[0])
part_one = 0
part_two = 0

def grid_val(grid, r, c,) :
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) :
        return grid[r][c]
    else :
        return " "

for r in range(M) :
    for c in range(N) :
        if (r, c) in seen :
            continue

        area = 0 

        q = collections.deque()
        q.append((r ,c))

        shape = set()

        while q :
            nr, nc = q.popleft()

            if (nr, nc) in shape :
                continue

            area += 1
            shape.add((nr, nc))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
                rr, cc = nr + dr, nc + dc

                if (
                    rr < 0 or 
                    cc < 0 or
                    rr == M or
                    cc == N or
                    (rr, cc) in shape or
                    grid[r][c] != grid[rr][cc]
                )   :
                    continue

                q.append((rr, cc))


        perimeter = 0
        corners = 0

        for xr, xc in shape :
            current = grid[xr][xc]
            up = grid_val(grid, xr - 1, xc)
            down = grid_val(grid, xr + 1, xc)
            left = grid_val(grid, xr, xc - 1)
            right = grid_val(grid, xr, xc + 1)

            
            if (current != up and current != right) :
                corners += 1
            if (current != right and current != down) :
                corners += 1
            if (current != down and current != left) :
                corners += 1
            if (current != left and current != up) :
                corners += 1



            if (current != grid_val(grid, xr - 1, xc - 1 ) and up == current and left == current) :
                corners += 1
            if (current != grid_val(grid, xr - 1, xc + 1) and up == current and right == current) :
                corners += 1
            if (current != grid_val(grid, xr + 1, xc + 1) and down == current and right == current) :
                corners += 1
            if (current != grid_val(grid, xr + 1, xc - 1) and down == current and left == current) :
                corners += 1

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
                rr, cc = xr + dr, xc + dc
                if (
                    rr < 0 or 
                    cc < 0 or
                    rr == M or
                    cc == N or
                    grid[r][c] != grid[rr][cc]
                )   :
                    perimeter += 1






        seen = seen.union(shape)
        part_one += (area * perimeter)
        part_two += (area * corners)


            
print(f"part one answer is {part_one}")
print(f"part two answer is {part_two}")


