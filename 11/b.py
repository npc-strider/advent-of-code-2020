
from copy import deepcopy

mat = [ ['.']+list(x)+['.'] for x in open('input').read().replace('L','#').splitlines() ] #
null = [ '.' for x in range(len(mat[0])) ]
# cmat = [null] + [ ['.']+[ '0' for y in range(len(mat[0])-2) ]+['.'] for x in mat ] + [null]
mat = [null] + mat + [null]

def RTX_side(r, d, y, mat): # Yes i know this isn't proper raytracing but haha tech tip nvidia rtx 6900ti funny moment.
    top = True
    bottom = True
    side = True
    c = 0
    j_d = 1
    for i in r:
        if top and y+j_d in d:
            cell = mat[y+j_d][i]
            if cell == 'L':
                top = False
            elif cell == '#':
                top = False
                c += 1
            # mat[y+j_d][i] = "Y"
        if y-j_d in d and bottom:
            cell = mat[y-j_d][i]
            if cell == 'L':
                bottom = False
            elif cell == '#':
                bottom = False
                c += 1
            # mat[y-j_d][i] = "Y"
        if side:
            if mat[y][i] == "L":
                side = False
            if mat[y][i] == "#":
                side = False
                c += 1
            # mat[y][i] = 'Y'
        if c == 3: break
        j_d += 1
    return c

def RTX_top(r, i, mat):
    for j in r:
        if mat[j][i] == 'L':
            return 0
        elif mat[j][i] == '#':
            return 1
        # mat[j][i] = "Y"
    return 0

# mat_ = list(map(list, zip(*mat)))

dim_j = len(mat)-1
# dim_j = len(mat_)-2
dim_i = len(mat[0])-1

domVERT = range(1,dim_j+1)  #Domain for vertical / j values
# [ print(x) for x in mat ]
def RTX_ON(mat):
    mat_ = deepcopy(mat)
    d = False
    for x in range(1, dim_i):
        for y in range(1, dim_j):
            # [ print(x) for x in mat ]
            # mat[y][x] = 'X'
            rN = range(y-1,0,-1)
            rS = range(y+1,dim_j+1)

            rE = range(x+1, dim_i+1)
            rW = range(x-1, 0, -1)

            # print(list(rN), list(rS))
            # print(list(rE), list(rW))

            c = (RTX_side(rE, domVERT, y, mat) + RTX_side(rW, domVERT, y, mat) + RTX_top(rN, x, mat) + RTX_top(rS, x, mat))
            # cmat[y][x] = (str)(c)
            if mat[y][x] == '#' and c > 4:
                mat_[y][x] = 'L'
                d = True
            elif mat[y][x] == 'L' and c == 0:
                mat_[y][x] = '#'
                d = True
    if d == True:
        # print("")
        # print("")
        # [ print(x) for x in mat ]
        # [ print(x) for x in cmat ]
        # print("")
        # [ print(x) for x in mat_ ]
        # print("")
        mat = RTX_ON(mat_)
        return mat
    return mat


simulated = RTX_ON(mat) #This is slow AF

[ print(''.join(x)) for x in simulated ] #output ascii
print(sum([ x.count('#') for x in simulated ]))
