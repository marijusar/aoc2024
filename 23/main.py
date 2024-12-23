import sys
import collections
from typing import List

file_path = sys.argv[1]
file = open(file_path)
edges = [[edge for edge in x.strip().split("-")] for x in file.readlines()]


adj_list = collections.defaultdict(list)
connections = set()

for fr, to in edges :
    adj_list[fr].append(to)
    adj_list[to].append(fr)


def dfs(node, path) :
    if path[0] == node and len(path) == 4:
        path.pop()
        connections.add(tuple(sorted(path)))
        return 

    if node == path[0] and len(path) > 1:
        return

    if len(path) > 3 :
        return


    for neighbour in adj_list[node] :
        n_p = path[::]
        if neighbour not in n_p or (neighbour in n_p and len(n_p) == 3):
            n_p.append(neighbour)
            dfs(neighbour, n_p)


for start in adj_list.keys() :
    dfs(start, [start])

part_one = 0

for nodes in connections :
    for computer in nodes :
        if computer[0] == "t" :
            part_one += 1
            break

print(f"part one answer is {part_one}")


def is_network(maybe_network : List[str]) -> bool :
    for n1 in maybe_network :
        for n2 in maybe_network :
            if n1 == n2 :
                continue

            if n1 not in adj_list[n2] :
                return False


    return True


networks = set()

def backtrack(network, neighbors, i) :
    if i == len(neighbors) and is_network(network) :
        networks.add(tuple(sorted(network)))
        return

    if i == len(neighbors) :
        return

    if not is_network(network) :
        return

    network.append(neighbors[i])
    backtrack(network, neighbors, i + 1)
    network.pop()
    backtrack(network, neighbors, i + 1)

for start in adj_list.keys() :
    backtrack([start], adj_list[start], 0)



longest_network = ()

for n in networks :
    if len(n) > len(longest_network) :
        longest_network = n


part_two = ",".join(longest_network)

print(f"part two answer is {part_two}")


