import sys

file_path = sys.argv[1]
file = [x.strip().split("\n") for x in open(file_path).read().split("\n\n")]

keys = []
locks = []

for key_or_lock in file :
    heights = []
    for i in range(len(key_or_lock[0])) :
        h = -1
        for j in range(len(key_or_lock)) :
            if key_or_lock[j][i] == "#" :
                h += 1
        heights.append(h)
    if all([char == "#" for char in key_or_lock[0]]) :
        locks.append(heights)
    else :
        keys.append(heights)



part_one = 0

for k in keys :
    for l in locks:
        acc = []
        for i in range(len(k)) :
            if k[i] + l[i] > 5 :
                acc.append(False)
            else :
                acc.append(True)

        if all(acc) :
            part_one += 1


print(f"part one answer is {part_one}")





