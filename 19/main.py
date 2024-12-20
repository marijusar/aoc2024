import sys

file_path = sys.argv[1]
patterns, towels = open(file_path).read().split("\n\n")

p = set([x.lstrip() for x in patterns.strip().split(",")])
t = towels.strip().split("\n")


def dfs_one(i, j, towel) :
    if i == len(towel):
        return True


    if j > len(towel) :
        return False

    
    ans = False

    if towel[i:j] in p :

        ans = dfs_one(j, j + 1, towel)


    return ans or dfs_one(i, j + 1, towel)


cache = {}

def dfs_two(i, j, towel) :
    if (i, j, towel) in cache :
        return cache[(i, j, towel)]

    if i == len(towel):
        return 1


    if j > len(towel) :
        return 0

    
    ans = 0

    if towel[i:j] in p :
        ans += dfs_two(j, j + 1, towel)


    cache[(i, j, towel)] = ans + dfs_two(i, j + 1, towel)

    return cache[(i, j, towel)]

part_one = 0
part_two = 0

for towel in t : 
    if dfs_one(0, 0, towel) :
        part_one += 1

    part_two += dfs_two(0, 0, towel)

print(f"part one answer is {part_one}")
print(f"part one answer is {part_two}")


