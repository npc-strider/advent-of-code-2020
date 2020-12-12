from itertools import chain
from copy import deepcopy

mat = [ list(x) for x in open('input').read().replace('L','#').splitlines() ]

def adj(adjrows, i):
    return list(chain(*[[ x[i] for i in range(i-1,i+2) ] for x in adjrows ]))

def simulate(mat):  # Part A.
    idom = range(len(mat[0]))
    jdom = range(len(mat))
    adjrows = [None, [ '.' for x in idom ]+['.'], mat[0]+['.']]
    mat_ = deepcopy(mat)
    d = 0
    for j in jdom:
        adjrows.pop(0)
        adjrows.append(mat[j+1]+['.']) if j+1 in jdom else adjrows.append([ '.' for x in idom ]+['.'])
        # print(adjrows)
        for i in idom:
            cell = mat[j][i]
            # print(i,j, cell)
            if cell == "#":
                # print(adj(adjrows))
                # print( [[ x[i] for i in range(i-1,i+2) ] for x in adjrows ] )
                adjm = adj(adjrows, i).count('#')-1
                if adjm > 3:
                    mat_[j][i] = 'L'
                    d += 1
            elif cell == "L":
                adjm = adj(adjrows, i).count('#')
                if adjm == 0:
                    mat_[j][i] = '#'
                    d += 1
    # [ print(x) for x in mat_ ]
    if d > 0:
        mat = simulate(mat_)
        return mat
    return mat

def a(mat): #Holy [] this is slow!
    # [ print(''.join(x)) for x in simulate(mat) ]
    count = []
    [ count.append(x.count('#')) for x in simulate(mat) ]
    return sum(count)

# SEE b.py FOR PART 2 ANSWER
# SEE b.py FOR PART 2 ANSWER
# SEE b.py FOR PART 2 ANSWER
# NOT USING THIS AS MY ANSWER.

# # print(a(mat))

# def diagrtx(mat, r, nc, pc, jdom):
#     [c, pb, nb] = [0, False, False]
#     for x in r:
#         y = -x + nc
#         if nb == False and -y in jdom:
#             cell = mat[-y][x]
#             if cell == '#':
#                 c += 1
#                 nb = True
#             elif cell == "L":
#                 nb = True
#         y = x + pc
#         if pb == False and -y in jdom:
#             cell = mat[-y][x]
#             if cell == '#':
#                 c += 1
#                 pb = True
#             elif cell == "L":
#                 pb = True
#     return c

# def hrtx(mat, r, j, idom):
#     for x in r:
#         if x in idom:
#             cell = mat[j][x]
#             if cell == "#":
#                 return 1
#                 break
#             elif cell == "L":
#                 break
#     return 0

# def vrtx(mat, r, i, jdom):
#     for y in r:
#         if -y in jdom:
#             cell = mat[-y][i]
#             if cell == "#":
#                 return 1
#                 break
#             elif cell == "L":
#                 break
#     return 0

# def RTX(mat, idom, jdom, i, j): #generate diagonals - this is quality '3am' code right here
#     nc = i + j
#     pc = j - i
#     # print(nc, pc)
#     # print(list(range(i,len(mat[0]))))
#     # [ print(x) for x in mat ]
#     rl = range(i-1, -1, -1)
#     lr = range(i+1, len(mat[0]))
#     u = range(j+1, 1)
#     d = range(j-1, -len(mat), -1)
#     return (
#         diagrtx(mat, rl, nc, pc, jdom) + hrtx(mat, rl, -j, idom)
#         + diagrtx(mat, lr, nc, pc, jdom) + hrtx(mat, lr, -j, idom)
#         + vrtx(mat, u, i, idom) + vrtx(mat, d, i, idom)
#     )
#     #wtf part over.

# def simulate2(mat):
#     idom = range(len(mat[0]))
#     jdom = range(len(mat))
#     mat_ = deepcopy(mat)
#     d = 0
#     for j in jdom:
#         for i in idom:
#             c = RTX(mat, idom, jdom, i, j)
#             cell = mat[j][i]
#             # print(i,j, c, cell)
#             if cell == "#":
#                 if c > 4:
#                     mat_[j][i] = 'L'
#                     d += 1
#             elif cell == "L":
#                 if c == 0:
#                     mat_[j][i] = '#'
#                     d += 1
#     [ print(''.join(x)) for x in mat_ ]
#     print('')
#     if d > 0:
#         mat = simulate2(mat_)
#         return mat
#     return mat

#     #increment x
#     # print([-x + nc if -(-x + nc) in jdom else None, x + pc if -(x + pc) in jdom else None])

#     # print({x:[-x + nc if -(-x + nc) in jdom else None, x + pc if -(x + pc) in jdom else None] for x in idom})

# def b(mat): #Holy shit this is even slower!
#     count = []
#     [ count.append(x.count('#')) for x in simulate2(mat) ]
#     return sum(count)

# print(b(mat))

# # def rtx(mat, i, j): #raytracer
