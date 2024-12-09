import sys
import heapq
from collections import deque


file_path = sys.argv[1]
file = open(file_path)
line = file.readline().strip()


numbers = []
free_space = []

current_block = 0

for i, char in enumerate(line) :
    n = int(char)
    if i % 2 == 0 :
        heapq.heappush(numbers, [-current_block, -(current_block + n), i // 2])
        current_block += n
    else :
        heapq.heappush(free_space, [current_block,  current_block + n])
        current_block += n
    
while free_space :
    n_s, n_e, id = heapq.heappop(numbers)
    n_s, n_e, = -n_s, -n_e
    space_start, space_end = heapq.heappop(free_space)
    diff = n_e - n_s

    if space_start > n_e :
        heapq.heappush(numbers, [-n_s, -n_e, id])
        continue

    if space_end - space_start > diff :
        n_n_s = space_start + diff
        heapq.heappush(free_space, [n_n_s, space_end])
        heapq.heappush(numbers, [-space_start, -n_n_s, id])
    elif space_end- space_start == diff :
        heapq.heappush(numbers, [-space_start, -space_end, id])
        k = n_s
    else :
        space_size = space_end - space_start
        heapq.heappush(numbers, [-space_start, -space_end, id])
        heapq.heappush(numbers, [-n_s, -(n_e - space_size), id])

numbers = [[-x, -y, z] for x, y, z in numbers]
numbers.sort()

part_one = 0

for start, end, id in numbers :
    for i in range(start, end) :
        part_one += id * i

        
print(f"part one answer is {part_one}")

file = open(file_path)
line = file.readline().strip()

numbers = []
free_space = deque()
current_block = 0

for i, char in enumerate(line) :
    n = int(char)
    if i % 2 == 0 :
        numbers.append([current_block, current_block + n, i // 2, False])
        current_block += n
    else :
        free_space.append([current_block,  current_block + n])
        current_block += n
i = len(numbers) - 1

while i >= 0 :
    temp_queue = deque()
    n_s, n_e, id, moved = numbers[i]
         
    while free_space and not moved and free_space[0][0] < n_s:
        free_space_start, free_space_end = free_space.popleft()

        if free_space_end - free_space_start > n_e - n_s :
            numbers.append([free_space_start, free_space_start + (n_e - n_s), id, False])
            numbers[i][3] = True
            temp_queue.append([free_space_start + (n_e - n_s), free_space_end])
            i += 1
            break
        elif free_space_end - free_space_start == n_e - n_s :
            numbers.append([free_space_start, free_space_end, id, False])
            numbers[i][3] = True
            i += 1
            break

        temp_queue.append([free_space_start, free_space_end])

    while free_space :
        temp_queue.append(free_space.popleft())
    free_space = temp_queue
    i -= 1
    numbers.sort()

numbers = [[x, y, z] for x, y, z, moved in numbers if not moved]
        

part_two = 0

for start, end, id in numbers :
    for i in range(start, end) :
        part_two += id * i


    
print(f"part two answer is {part_two}")



