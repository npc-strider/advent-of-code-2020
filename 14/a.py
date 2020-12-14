
from itertools import product

d = [ x.replace('[', ' = ').replace(']', '').split(' = ') for x in open('input').read().splitlines() ]

def sum(ram, b):
    c = 0
    for x in ram:
        # print(ram[x])
        c += int(ram[x], b)
    return c
    # print(sum({int(ram[s], 2) for s in ram}))


def a(d):
    ram = {}
    mask = []
    for instruction in d:
        cmd = instruction[0]
        # print(instruction)
        if cmd == 'mask':
            mask = list(instruction[1])
        elif cmd == 'mem':
            # print(int(instruction[1]))
            b = list(bin(int(instruction[2]))[2:].zfill(36))
            for x in range(len(mask)):
                if mask[x] != 'X':
                    b[x] = mask[x]
            ram[int(instruction[1])] = ''.join(b)
    return sum(ram, 2)

def b(d):
    ram = {}
    mask = []
    for instruction in d:
        cmd = instruction[0]
        # print(instruction)
        if cmd == 'mask':
            mask = list(instruction[1])
        elif cmd == 'mem':
            b = list(bin(int(instruction[1]))[2:].zfill(36))
            for x in range(len(mask)):
                if mask[x] != '0':
                    b[x] = mask[x]
            b = ''.join(b)
            b_ft = b.replace('X', '{}') 
            for i in product('01', repeat=b.count('X')):
                addr = int(b_ft.format(*i),2)
                ram[addr] = instruction[2]
    return sum(ram, 10)

print(a(d), b(d))