import sys
import re

numbers = r"\d+"
file_path = sys.argv[1]
file = open(file_path)
content = file.read().split("\n\n")

games = [[int(y) for y in re.findall(numbers, x)] for x in content]

part_one = 0
part_two = 0



def solve(game, diff) :
# x * 94 + y * 22 = 8400 
# x * 34 + y * 67 = 5400
# a * ax + b * bx = px
# a * ay + b * by = py

# b = (py - (a * ay)) / by

    ax, ay, bx, by, px, py = game
    px, py = px + diff, py + diff


    a = ((px * by) - (py * bx)) / ((by * ax) - (ay * bx)) 
    b = (py - (a * ay)) / by

    if a % 1 == 0 and b % 1 == 0 :
        return a * 3 + b
    else :
        return 0
    
    


for game in games :
    part_one += solve(game, 0)
    part_two += solve(game, 10000000000000)

print(f"part one answer is {part_one}")
print(f"part two answer is {part_two}")


