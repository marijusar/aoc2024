from collections import defaultdict
import sys
from typing import List

file_path = sys.argv[1]
numbers = list(map(int ,open(file_path).readlines()))

ans = []

def calculate_secret_numbers(n : int, k : int) :
    for _ in range(k) :
        t = n * 64
        n ^= t
        n %= 16777216
        t = int(n / 32)
        n ^= t
        n %= 16777216
        t = n * 2048
        n ^= t
        n %= 16777216
    return n


for n in numbers :
    ans.append(calculate_secret_numbers(n, 2000))


part_one = sum(ans)

print(f"part one answer is {part_one}")

def make_price_change_key(arr : List[int]) -> str :
    return "".join(map(str, arr))

def get_price_changes(n : int) :
    numbers = [n % 10]
    acc = {}

    for _ in range(2000) :
        t = n * 64
        n ^= t
        n %= 16777216
        t = int(n / 32)
        n ^= t
        n %= 16777216
        t = n * 2048
        n ^= t
        n %= 16777216
        numbers.append(n % 10)

    changes = []
    for i in range(1, len(numbers)) :
        changes.append(numbers[i] - numbers[i - 1])

    changes = [0] + changes

    for i in range(4, len(numbers)) :
        sub_arr = changes[i-3:i+1]
        key = make_price_change_key(sub_arr)
        
        if key not in acc :
            acc[key] = numbers[i]


    return acc


g = defaultdict(int)
for n in numbers :

    ledger = get_price_changes(n)

    for k, v in ledger.items() :
        g[k] += v

part_two = 0
key = ""

for k, v in g.items() :
    if v > part_two :
        part_two = v 
        key = k


print(f"part two answer is {part_two}")

