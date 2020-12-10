from collections import Counter
import itertools
import math

lines = { int(x) for x in open('input').read().splitlines() }
lines.add(0)

def a(transformers):
    v = 0
    dv = [3] #Always a 3v transformer at the end
    while v < max(transformers):
        v_ = min(set(range(v+1,v+4)).intersection(transformers))
        dv.append(v_ - v)
        v = v_
    count = dict(Counter(dv))
    return count[3]*count[1]

def b(c, v, transformers):
    for v_ in set(range(v+1,v+4)).intersection(lines):
        if v_ == max(transformers):
            c += 1
        else:
            c = b(c, v_, transformers)
    return c
# print(b(0, 0, lines))
##  This is a recursive solution. IT works but it'll take an eternity to go through the whole list of transformers.
##  My solution: Split the set by 'gaps' (where there is only one path through to the next number), then multiply together. defintely not the most optimal but it's logical for me and it works! :)
def b_optimized(transformers):
    rel = { v: set(range(v+1,v+4)).intersection(transformers) for v in transformers }
    rel.pop(max(transformers))
    gaps = { list(rel[x])[0] if (len(rel[x]) == 1) else None for x in rel }.intersection(transformers)
    gaps.add(list(rel)[0])
    gaps = sorted(gaps)
    idx = 0
    C = 1
    while idx+1 < len(gaps):
        s = sorted(set(range(gaps[idx],gaps[idx+1]+1)).intersection(transformers))
        if len(s) > 2:
            C *= b(0, list(s)[0], s)
        idx += 1
    return C

print(a(lines))
print(b_optimized(lines))