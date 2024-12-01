import sys
from typing import Counter

file_name = sys.argv[1]

f = open(file_name)
lines = [[int(y) for y in x.strip().split("  ")] for x in f.readlines()]

first_list = sorted([x[0] for x in lines])
second_list = sorted([x[1] for x in lines])

part_one =  0 

for i in range(len(first_list)) :
    part_one += abs(second_list[i] - first_list[i])

print(f"part one asnwer : {part_one}", )

second_list_counter = Counter(second_list)

part_two = 0

for n in first_list :
    if n in second_list_counter :
        a = (n * second_list_counter[n])
        part_two += a


print(f"part two answer : {part_two}", )

