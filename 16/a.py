import itertools
from copy import deepcopy

ranges = { y[0]:[range(int(z[0]), int(z[1])+1) for r in y[1:] if ( z:= r.split('-') )] for x in open('input_ranges').read().splitlines() if ( y:= x.replace(' or ',': ').split(': ') ) }
tickets = [ [ int(y) for y in x.split(',') ] for x in open('input_tickets').read().splitlines() ]

total_range = []
for range_ in ranges:
    [ total_range.append(list(x)) for x in ranges[range_] ]
total_range = list(itertools.chain.from_iterable(total_range))

error = []
valid = deepcopy(tickets)
i = 0
for ticket in tickets[1:]:
    i += 1
    err_buf = len(error)
    [ error.append(x) for x in ticket if x not in total_range ]
    if len(error) > err_buf:
        valid[i] = None
print(sum(error))
valid = [x for x in valid if (x != None)]
final_ranges = []
for i in range(0,len(valid[0])):
    col = []
    for j in range(0,len(valid)):
        col.append(valid[j][i])

    # print(col[0:4])
    valid_ranges = []
    for r in ranges:
        error = []
        range_ = ranges[r]
        [ error.append(x) for x in col if (x not in range_[0] and x not in range_[1]) ]
        if len(error) == 0:
            # print("         ",i, error, range_, r)
            valid_ranges.append(r)
    final_ranges.append(valid_ranges)
    # print(col)



p2 = 1
for z in range(len(final_ranges)):
    i_ = 0
    for x in final_ranges:
        if len(x) == 1:
            if x[0].split(' ')[0] == 'departure':
                p2 *= tickets[0][i_]
            # print(i_, tickets[0][i_], x)
            for i in range(len(final_ranges)):
                if x[0] in final_ranges[i]:
                    # print(final_ranges[i])
                    final_ranges[i] = [ k for k in final_ranges[i] if k != x[0] ]
        i_ += 1
print(p2)