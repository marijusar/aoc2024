import collections
import sys

file_path = sys.argv[1]

file = open(file_path)
lines = file.read()

r, p = lines.split("\n\n")

rules = [[int(y) for y in x.split("|")]for x in r.split("\n")]
adj_list = collections.defaultdict(set)
reverse_adj_list = collections.defaultdict(set)
for fr, to in rules :
    adj_list[to].add(fr)
    reverse_adj_list[fr].add(to)

pages = [[int(y) for y in x.split(",")] for x in p.strip().split("\n")]


def is_valid_page(page, rules) :
    previous = set()
    for item in page :
        for previous_item in rules[item] :
            if previous_item in page and previous_item not in previous :
                return False
        previous.add(item)

    return True


part_one = 0 


for page in pages :
    if is_valid_page(page, adj_list) :
        part_one += page[len(page) // 2]

print(f"part one answer is {part_one}")

def topological_sort(page, rules, reverse_rules) :
    in_degrees = {}

    for p in page :
        in_degrees[p] = 0
        if p in rules :
            for item in page :
                if item in rules[p] :
                    in_degrees[p] += 1
            
    q = collections.deque()

    for degree in in_degrees :
        if in_degrees[degree] == 0 :
            q.append(degree)

    ans = []

    while q :
        item = q.popleft()
        for r in reverse_rules[item] :
            if r in in_degrees :
                in_degrees[r] -= 1
                if in_degrees[r] == 0 :
                    q.append(r)

        ans.append(item)

    return ans

part_two = 0

for page in pages :
    if not is_valid_page(page, adj_list) :
        t_sorted = topological_sort(page, adj_list, reverse_adj_list)
        part_two += t_sorted[len(t_sorted) // 2]
        

print(f"part two answer is {part_two}")





