import sys

file_path = sys.argv[1]

file = open(file_path)

line = file.readline().strip()

stones = line.split(" ")

s = stones[::]

for i in range(25) :
    temp = []
    while s :
        stone = s.pop() 

        if stone == "0" :
            temp.append(str(1))
        elif len(stone) % 2 == 0 :
            half = len(stone) // 2 
            left = stone[:half]
            right = stone[half:].lstrip("0")
            right = right if len(right) >= 1 else "0"
            temp += [left, right]
        else :
            stone = str(int(stone) * 2024)
            temp.append(stone)

    temp.reverse()
    s = temp


part_one = len(s)

print(f"part one answer is {part_one}")

cache = {}
ans = []

def split_stone(stone) :
    new_stones = []

    if stone == "0" :
        new_stones.append("1")
    elif len(stone) % 2 == 0 :
        half = len(stone) // 2 
        left = stone[:half]
        right = stone[half:].lstrip("0")
        right = right if len(right) >= 1 else "0"
        new_stones += [left, right]
    else :
        stone = str(int(stone) * 2024)
        new_stones.append(stone)

    return new_stones


def dfs(i, stone) :
    if i == 0 :
        return 1

    if (stone, i) in cache :
        return cache[(stone, i)]

    new_stones = split_stone(stone)
    acc = 0

    for n_s in new_stones :
        s = dfs(i - 1, n_s)
        acc += s

    cache[(stone, i)] = acc

    return cache[(stone, i)]
        

part_two = 0
    
for stone in stones :
    part_two += dfs(75, stone)

print(f"part two answer is {part_two}")


    


     
        




