import sys 
import heapq
import copy

file_path = sys.argv[1]
file = open(file_path)

grid = [[y for y in x.strip()] for x in file.readlines()]

M, N = len(grid), len(grid[0])


def find_min_score(start, grid) :
    r, c = start
    seen = {}
    heap = [[0, r, c, 1, [(r, c, 0, 1)]]]
    paths = set()
    best_score = float("inf")

    while heap:
        score, pr, pc, direction, path = heapq.heappop(heap)

        if (pr, pc, direction) in seen and seen[(pr, pc, direction)] < score :
            continue

        seen[(pr, pc, direction)] = score

        if grid[pr][pc] == "E" :
            if score > best_score :
                return [score, paths]
            for r, c, _, _ in path :
                paths.add((r, c))
            best_score = score



        for i, (dr, dc) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]) :
            rr, cc = pr + dr, pc + dc

            new_score = score + 1 if i == direction else score + 1001

            if (grid[rr][cc] == "#" or 
                    (rr, cc, i) in seen ) : 
                continue


            n_p = copy.deepcopy(path)
            n_p.append((rr, cc, new_score, i))


            heapq.heappush(heap, [new_score, rr, cc, i, n_p])

    return []


part_one = 0
part_two = 0


    
tiles = set()

for r in range(M) :
    for c in range(N) :

        if grid[r][c] == "S" :
            score, path = find_min_score([r, c], grid)
            print(len(path))

            part_two = len(path)




print(f"part one answer is {part_one}")
print(f"part two answer is {part_two}")

[print("".join(x)) for x in grid]






