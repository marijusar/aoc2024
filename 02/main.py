import sys
from typing import List, Callable

file_path = sys.argv[1]

file = open(file_path)
input = [[int(y) for y in x.split(" ")] for x in file.readlines()]

def is_monotonic(report : List[int], tolerance : int, fn : Callable[[int, int], bool]) :
    t = 0 
    stack = []

    for item in report :
        if not stack :
            stack.append(item)
            continue

        satisfies_monotonic_requirement = fn(stack[-1], item)

        if satisfies_monotonic_requirement  :
            stack.append(item)
        elif t < tolerance :
            t += 1
            continue
        else :
            return False


    return True


part_one = 0

def is_decreasing(a, b) :
    if 1 <= a - b <= 3 :
        return True

    return False

def is_increasing(a, b) :
    if 1 <= b - a <= 3 :
        return True

    return False


for r in input :
    if is_monotonic(r, 0, is_increasing) or is_monotonic(r, 0, is_decreasing) :
        part_one += 1


print(f"part one answer : {part_one}")

part_two = 0

def dfs(i, fn, skipped, row, prev):
    if i >= len(row) :
        return True

    if prev == -1 and skipped :
        return dfs(i + 1, fn, skipped, row, i) 

    if prev == -1 and not skipped :
        return dfs(i + 1, fn, skipped, row, i) or dfs(i + 2, fn, not skipped, row, i)

    if not fn(row[prev], row[i]) :
        return False

    ans = False

    if not skipped :
        ans = ans or dfs(i + 2, fn, not skipped, row, i)

    ans = ans or dfs(i + 1, fn, skipped, row, i)

    return ans


def is_valid_report(row) :
    return (dfs(0, is_increasing, False, row, -1) or 
            dfs(0, is_decreasing, False, row, -1) or 
            dfs(1, is_decreasing, True, row, -1) or 
            dfs(1, is_increasing, True, row, -1))


for r in input :
    if is_valid_report(r) :
        part_two += 1

print(f"part two answer : {part_two}")
