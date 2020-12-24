import itertools
from copy import deepcopy

cups = [ int(x) for x in list(str(389125467)) ]

size = len(cups)

def showcursor(cups, idx):
    cups_ = deepcopy(cups)
    cups_[idx] = '('+str(cups_[idx])+')'
    return cups_

maxv = max(cups)

def getdest(cups, value):
    idx_ = value - 1
    while True:
        if idx_ in cups:
            return cups.index(idx_)
        else:
            idx_ -= 1
            if idx_ < 0:
                idx_ = maxv

def pick(cups, idx):
    buf = []
    d = 0
    for i in range(0,3):
        if idx in range(len(cups)):
            buf.append(cups.pop(idx))
        else:
            buf.append(cups.pop(0))
            d += 1
    return [buf,d]

pointer = 0
i = 0
# while i < 100:
while i < 10^6:
    # print(showcursor(cups, pointer))
    val = cups[pointer]
    buf = pick(cups,pointer+1)
    if pointer+1 in range(len(cups)):
        next_ptr_value = cups[pointer+1]
    else:
        next_ptr_value = cups[0]

    dest = getdest(cups,val)+1
    # print('dest:', dest, cups[dest-1])
    # print(next_ptr_value)
    # print('buf:', buf)
    if dest < len(cups):
        [cups.insert(dest,x) for x in buf[0][::-1]]
    else:
        # print('alt')
        [cups.append(x) for x in buf[0]]
    i += 1
    pointer = cups.index(next_ptr_value)
    # print('nextptr', pointer, next_ptr_value)
    # print(showcursor(cups, pointer))
    # print()

print(cups)
pointer = cups.index(1)
print(int(''.join([ str(cups[x%len(cups)]) for x in range(pointer,pointer+len(cups)) ][1:])))