import itertools
from copy import deepcopy

def convert_to_list(lpt,start): #For research purposes
    next_v = lpt[start][1]
    li = [start,next_v]
    c = 0
    while next_v != start:
        c += 1
        next_v = lpt[next_v][1]
        li.append(next_v)
        if c > 15:
            break
    return li[:-1]

cups_l = [ int(x) for x in list(str(389125467)) ]
cups = { cups_l[i]:[cups_l[i-1],cups_l[i+1]] for i in range(len(cups_l)-1) }
cups.update({cups_l[-1]:[cups_l[-2],cups_l[0]]}) # Let's make a linked list! Today I learned : linked lists are pretty cool!
next_cursor = cups_l[0] # Initialize cursor at cursor of tape.

def relink(cups, idx1, idx2): # Make link from idx1 to idx2
    cups[idx1][1] = idx2
    cups[idx2][0] = idx1
    return cups

def next(cups,cursor,n):
    for i in range(0,n+1):
        cursor = cups[cursor][1]
    return cursor

max_val = max(cups.keys())
def get_destination(idx,picked):
    idx -= 1
    while True:
        if idx > 0 and idx not in picked:
            return idx
        else:
            idx -= 1
            if idx <= 0:
                idx = max_val

z = 0
while z < 3:
    cursor = next_cursor
    next_cursor = next(cups,cursor,3)
    picked = [ next(cups,cursor,n) for n in range(0,3) ]
    dest = get_destination(cursor,picked)
    after_picked = next(cups, cursor, 3)
    after_dest = next(cups,dest,1)
    after_picked_dest = next(cups, dest, 3)
    print()
    print('CURSOR',cursor,'NEXT_CURSOR',next_cursor, 'PICK', picked, 'DEST', dest)
    print(after_picked, after_dest, after_picked_dest)
    print(convert_to_list(cups,cups_l[0]))

    print(cups, cursor, after_picked)
    cups = relink(cups, cursor, after_picked) # after picked
    # print(cups, dest, picked[0])
    # cups = relink(cups, dest, after_dest)
    cups = relink(cups, dest, picked[0])
    # print(cups, picked[2], after_picked_dest)
    cups = relink(cups, picked[2], after_picked_dest)
    z += 1
    print(cups)