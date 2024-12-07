import sys

file_path = sys.argv[1]
file = open(file_path)

lines = [x.strip().split(":") for x in file.readlines()]
lines = [[int(z[0]), [int(y) for y in z[1].lstrip().split(" ")] ] for z in lines]


def dfs_one(i, j, s) :
    if j == len(lines[i][1]) and s == lines[i][0]:
        return True

    if s > lines[i][0] or j == len(lines[i][1]) :
        return False


    return dfs_one(i, j + 1, s + lines[i][1][j]) or dfs_one(i, j + 1, s * lines[i][1][j])

def dfs_two(i, j, s) :
    if j == len(lines[i][1]) and s == lines[i][0]:
        return True

    if s > lines[i][0] or j == len(lines[i][1]) :
        return False


    return dfs_two(i, j + 1, s + lines[i][1][j]) or dfs_two(i, j + 1, s * lines[i][1][j]) or dfs_two(i, j + 1, int(str(s) + str(lines[i][1][j])))

part_one = 0
part_two = 0

for i in range(len(lines)) :
    if dfs_one(i, 0, 0) :
        part_one += lines[i][0]

    if dfs_two(i, 0, 0) :
        part_two += lines[i][0]

print(f"part one answer is {part_one}")
print(f"part two answer is {part_two}")
