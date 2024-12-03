import sys
import re

file_path = sys.argv[1]
file = open(file_path)
content = file.read()

regex = r'mul\(\d+,\d+\)'

tuples = [[int(y) for y in x.lstrip("mul(").strip(")").split(",")] for x in re.findall(regex, content)]

part_one = sum([x * y for x, y in tuples])

print(f"part one answer is : {part_one}")

regex = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"

match = re.findall(regex, content)

flags = {
    "don't()" : False,
    "do()" : True
}

tuples = []
enabled = True

for m in match :
    if m in flags :
        enabled = flags[m]
    elif enabled :
        tuples.append(m)

tuples = [[int(y) for y in x.lstrip("mul(").strip(")").split(",")] for x in tuples]

part_two = sum([x * y for x, y in tuples])

print(f"part two answer is : {part_two}")
