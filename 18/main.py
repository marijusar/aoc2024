import sys
import collections


file_path = sys.argv[1]
b = [tuple(map(int, x.strip().split(","))) for x in open(file_path).readlines()]

N = 71


def get_shortest_path_length(blockers) :
    i = 0
    seen = set()
    q = collections.deque()
    q.append((0, 0))

    while q :
        for _ in range(len(q)) :
            x, y = q.popleft()

            if (x ,y) in blockers or (x, y) in seen:
                continue


            if (x, y) == (N - 1, N - 1) :
                return i


            seen.add((x, y))

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
                nx, ny = x + dx, y + dy 

                if (
                    nx < 0 or 
                    nx == N or
                    ny < 0 or
                    ny == N or 
                    (nx, ny) in seen or 
                    (nx, ny) in blockers
                ) :
                    continue

                q.append((nx, ny))


        i += 1

part_one = get_shortest_path_length(set(b[:1024]))
print(f"part one answer is {part_one}")

for i in range(len(b)) :
    if not get_shortest_path_length(set(b[:i])) :
        print(f"part two answer is {b[i - 1]}")
        break




