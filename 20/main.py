import sys
import collections

file_path = sys.argv[1]
file = open(file_path)
grid = [x.strip() for x in file.readlines()]

M, N = len(grid), len(grid[0])


path = []
seen = set()
q = collections.deque()

for r in range(M) :
    for c in range(N) :
        if grid[r][c] == "S" :
            q.append((r, c))


seconds = 0

while q :
    for _ in range(len(q)) :
        p = q.popleft()
        r, c = p

        if p in seen :
            continue

        path.append(p)
        seen.add(p)

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
            rr, cc = r + dr, c + dc

            if (
                rr < 0 or 
                rr == M or 
                cc < 0 or 
                cc == N or
                grid[rr][cc] == "#" or
                (rr, cc) in seen
            ) :
                continue

            q.append((rr, cc))

    seconds += 1


part_one = 0

grid = [[y for y in x] for x in grid]
cheats = collections.defaultdict(int)

P = len(path)

for i in range(P) :
    r, c = path[i]

    grid[r][c] = i

for r, c in path :
    cheat = []
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
        rr, cc = r + dr, c + dc
        if grid[rr][cc] == "#" :
            cheat.append([rr, cc])

    for xr, xc in cheat :
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
            rr, cc = xr + dr, xc + dc
            if (rr < 0 or rr == M or cc < 0 or cc == N) : continue
            if grid[rr][cc] != "#" and grid[rr][cc] > grid[r][c] :
                if grid[rr][cc] - grid[r][c] - 2 >= 100 :
                    part_one += 1

print(f"part one answer is {part_one}")
                
part_two = 0
cheats = collections.defaultdict(int)

for i in range(P) :
    r, c = path[i]
    q = collections.deque()

    seconds = 20

    q.append((r, c, 0))
    seen = set()

    while q :
        xr, xc, s = q.popleft()

        if s > seconds :
            continue

        if (xr, xc) in seen :
            continue

        seen.add((xr, xc))

        if grid[xr][xc] != "#" and grid[xr][xc] > grid[r][c] + s :
            cheats[grid[xr][xc] - grid[r][c] - s]  += 1



        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
            rr, cc = xr + dr, xc + dc

            if (
                rr < 0 or 
                rr == M or 
                cc < 0 or 
                cc == N or 
                s + 1 > seconds 
            ) :
                continue

            q.append((rr, cc , s + 1))


            
for k, v in cheats.items() :
    if k >= 100 :
        part_two += v

print(f"part two answer is {part_two}")
