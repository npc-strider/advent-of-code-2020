import copy
import itertools

preamble_len = 25

d = [ int(x) for x in open('input').read().splitlines() ]

def sums(d):
    return [ sum(x) for x in list(itertools.combinations(d, 2)) ]

def a(d):
    index = preamble_len
    for n in d[preamble_len:]:
        if n not in sums(d[index-preamble_len:index]):
            print(n)
            return n
            break
        index += 1

def b(target,d):
    index = 0    
    current = []
    for i in range(len(d)):
        # print('-')
        # print(current)
        j = 0
        pop = []
        for j_ in current:
            # print(d[j_:i])
            s = sum(d[j_:i])
            if s == target:
                l = d[j_:i]
                print([l, min(l) + max(l)])
            elif s > target:
                pop.append(j)
                # print("POP")
                # print(current)
            j += 1
        [ current.pop(0) for x in pop ]
        current.append(i)


    #     if acc
    #         print(l)
    #         break
    #     if acc > target:
    #         acc = 0
    #         l = []
    # l = []
    # acc = 0
    # for n in d:
    #     l.append(n)
    #     acc += n
    #     if acc == target and n != target:
    #         print(l)
    #         break
    #     if acc > target:
    #         acc = 0
    #         l = []


b(a(d),d)