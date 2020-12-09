import copy
import itertools

preamble_len = 5

d = [ int(x) for x in open('input').read().splitlines() ]

index = preamble_len

def sums(d):
    return [ sum(x) for x in list(itertools.combinations(d, 2)) ]

s = sums(d[index-preamble_len:index])
for n in d[preamble_len:]:
    print(d[index-preamble_len:index])
    print(sorted(sums(d[index-preamble_len:index])))
    new = [ (x+y) for x in d[index-preamble_len:index-1] if (y := d[index-1]) ]
    print(new)
    print(sorted(s))
    print(n)

    index += 1
    s = copy.deepcopy(s)[4:]+new #4 is constant, combinations of 2 numbers