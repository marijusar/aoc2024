import collections
import sys
from collections import defaultdict
import itertools

file_path = sys.argv[1]
file = open(file_path).read()

wires, instructions = file.split("\n\n")

w_m = defaultdict(int)

for wire in wires.split("\n") :
    w, v = wire.split(":")
    w_m[w]= int(v.lstrip())

i_s = []
for instruction in instructions.strip().split("\n") :
    left, right = instruction.split("->")
    i_s.append([*left.strip().split(" "), right.lstrip()])

ops = {
    "AND" : lambda a, b : a & b,
    "OR" : lambda a, b : a | b,
    "XOR" : lambda a, b : a ^ b
}

def topological_sort(instruction_set, defaults) :
    in_degrees = defaultdict(int)
    index = defaultdict(list)

    for left, op, right, to  in instruction_set:
        in_degrees[to] += 1
        index[left].append([left, op,  right, to])
        index[right].append([left, op,  right, to])

    q = collections.deque()

    for d in defaults :
        q.append(d)

    order = []
    processed = set()

    while q :
        e = q.popleft()
        to_process = filter(lambda x : in_degrees[x[0]] == 0 and in_degrees[x[2]] == 0, index[e])


        for left, op, right, res in to_process :
            k = left + op + right + res
            if k in processed :
                continue
            processed.add(k)

            order.append([left, op, right, res])
            in_degrees[res] -= 1
            if in_degrees[res] == 0 :
                q.append(res)

    return order


i_s = topological_sort(i_s, w_m.keys())
ws = {}

for left, op, right, to in i_s :
    w_m[to] = ops[op](w_m[left], w_m[right])
    ws[to] = [op, left, right]


def get_number(char : str) -> int :
    ans = 0
    bits = [w_m[x] for x in sorted(w_m.keys()) if x[0] == char]
    B = len(bits)


    for i in range(B - 1, -1, -1) :
        ans |= (bits[i] << i)

    return ans


part_one = get_number("z")
print(f"part one answer is {part_one}")

## Kudos to HyperNeutrino for these helper functions and explanation..
def pp(wire, depth=0) :
    if wire[0] in "xy" : return "  " * depth + wire
    op, x , y = ws[wire]

    return "  " * depth + op + " (" + wire + ")\n" + pp(x, depth + 1) + "\n" + pp(y, depth + 1)


def make_wire(char, num) :
    return char + str(num).rjust(2, "0")

def verify_z(wire, num) :
    print("vz", wire, num)
    op, x, y = ws[wire]

    if op != "XOR" :return False
    if num == 0 :  return sorted([x, y]) == ["x00", "y00"]

    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify_intermediate_xor(wire, num) :
    print("vx", wire, num)
    op, x, y = ws[wire]

    if op != "XOR" :return False

    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num) :
    print("vc", wire, num)
    op, x , y = ws[wire]
    if num == 1 :
        return op == "AND" and sorted([x, y]) == ["x00", "y00"]    

    if op != "OR" : return False

    return verify_direct_carry(x, num - 1) and verify_recarry(y, num - 1) or  verify_direct_carry(y, num - 1) and verify_recarry(x, num - 1)


def verify_direct_carry(wire, num) :
    print("vd", wire, num)
    op, x, y = ws[wire]
    if op != "AND" : return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num) :
    print("vr", wire, num)
    op, x, y = ws[wire]
    if op != "AND" : return False
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)


def verify(num) :
    return verify_z(make_wire("z", num) , num)

i = 0 

while True :
    if not verify(i) : break
    i += 1


print("failed on", make_wire("z", i))

#wrp
#qkq
#vcg
#nsm

# z09 <-> rkf
# z20 <-> jgb
# z24 <-> vcg
# rrs <-> rvc

print(",".join(sorted(["z09", "z20", "rkf", "jgb", "z24", "vcg", "rrs", "rvc"])))

