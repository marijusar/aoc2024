import sys
import math
import re


file_path = sys.argv[1]
file = [re.findall(r"\d+", x) for x in open(file_path).read().strip().split("\n\n")]

registers, program = file
registers = list(map(int, registers))

A = registers[0]
B = registers[1]
C = registers[2]


def get_combo_operand(v : str) :
    if v in "0123" :
        return int(v)

    match v :
        case "4" :
            return A
        case "5" :
            return B
        case "6" :
            return C
        case _ :
            raise Exception(f"Invalid switch statement value {v}")


def adv(v : str):
    global A
    A = int(A / math.pow(2, get_combo_operand(v)))

def bxl(v : str) :
    global B
    B = B ^ int(v)

def bst(v : str) :
    global B
    B = get_combo_operand(v) % 8

def jnz(v :str) :
    if A != 0 :
        return [0, int(v)]


def bxc(_ : str) :
    global B 
    B = B ^ C

def out(v : str) :
    return [1, get_combo_operand(v) % 8]

def bdv(v : str) :
    global B
    B = int(A / math.pow(2, get_combo_operand(v)))

def cdv(v : str) :
    global C
    C = int(A / math.pow(2, get_combo_operand(v)))


instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


part_one = []

def get_program_output(program) :
    i = 0
    ans = []

    while i < len(program):
        pointer = program[i]
        operand = program[i + 1]

        op = instructions[int(pointer)]

        result = op(operand) 

        if result and result[0] == 1 :
            ans.append(result[1])

        if result and result[0] == 0 :
            i = result[1]
        else :
            i += 2


    return list(map(str, ans))


part_one = ",".join(get_program_output(program))

print(f"part one answer is {part_one}")


# 2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0
# b = a % 8
# b = b ^ 2
# c = a >> b
# b = b ^ 7
# b = b ^ c
# a = a >> 3
# out = b % 8
# pointer = 0

# Obviously needed help during this one
def solve(program, ans) :
    if program == [] : return ans
    for b in range(8) :
        a = ans << 3 | b
        b = b ^ 2
        c = a >> b
        b = b ^ 7 
        b = b ^ c
        
        if b % 8 == program[-1] :
            sub = solve(program[:-1], a)

            if sub is None :
                continue

            return sub

program = list(map(int, program))

part_two = solve(program, 0)
print(part_two)
