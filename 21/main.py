import sys
import collections
from typing import Dict, List, Tuple
import heapq
import functools

file_path = sys.argv[1]
file = [x.strip() for x in open(file_path).readlines()]

d_k = [[None, "^", "A"], ["<", "v", ">"]]
n_k = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

Graph = Dict[Tuple[str, str] , List[int]]


directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
arrows = ["<", "^", "v", ">"]

def shortest_path(fr : Tuple[int, int], to : Tuple[int, int], grid) -> List[int]:
    r, c = fr
    heap = [(0, r, c, [])]
    seen = set()
    possible_answers = []
    while heap :
        turn_count, nr, nc, path = heapq.heappop(heap)
        prev_direction = -1 if not path else path[-1]

        if (nr, nc, prev_direction) in seen :
            continue

        seen.add((nr, nc, prev_direction))

        if (nr, nc) == to :
            possible_answers.append((len(path),turn_count, *path))
            continue


        for i in range(len(directions)) :
            dr, dc = directions[i]
            rr, cc = nr + dr, nc + dc 

            if (
                rr < 0 or
                cc < 0 or 
                rr == len(grid) or 
                cc == len(grid[0]) or 
                grid[rr][cc] == None 
            ) :
                continue

            n_t = turn_count + 1 if path and path[-1] != i else turn_count
            n_p = [x for x in path]
            n_p.append(i)

            heapq.heappush(heap, (n_t, rr, cc, n_p))

    heapq.heapify(possible_answers)

    return list(possible_answers[0][2:])


def create_adj_list (grid : List[List[str | None]], adj_list : Graph) :
    for r in range(len(grid)) :
        for c in range(len(grid[r])) :
            for nr in range(len(grid)) :
                for nc in range(len(grid[r])) :
                    fr = grid[r][c]
                    to = grid[nr][nc]
                    if grid[r][c] != grid[nr][nc] and fr and to : 
                            adj_list[(fr, to)] = shortest_path((r, c), (nr, nc), grid)
    return adj_list

n_k_adj_list = create_adj_list(n_k, {})
d_k_adj_list = create_adj_list(d_k, {})

def map_path_to_arrows(path : List[int]) -> str :
    return "".join([arrows[x] for x in path])


def m(value : str, graph : Graph) -> str :
    value = "A" + value 

    instructions = []

    for i in range(1, len(value)) :
        fr, to = value[i - 1], value[i]
        if fr == to :
            instructions.append("A")
        else :
            p = map_path_to_arrows(graph[fr, to])
            p += "A"
            instructions.append(p)
    
    return "".join(instructions)


part_one = 0

for v in file :
    code = m(m(m(v, n_k_adj_list), d_k_adj_list), d_k_adj_list)
    num = int(v[:-1])

    part_one += num * len(code)

print(f"part one answer is {part_one}")

part_two = 0

cache = {}

def m_cached(move, i) :
    if i == 0 :
        return len(move)

    if (move, i) in cache :
        return cache[(move, i)]

    ans = 0
    code = [x + "A" for x in m(move, d_k_adj_list).split("A")][:-1]

    for mo in code :
        ans += m_cached(mo, i - 1)

    cache[(move, i)] = ans

    return cache[(move, i)]


for v in file :
    code = m(v, n_k_adj_list)
    code = [x + "A" for x in code.split("A")][:-1]
    l = sum([m_cached(x, 25) for x in code])

    num = int(v[:-1])

    part_two += num * l



print(f"part two answer is {part_two}")
