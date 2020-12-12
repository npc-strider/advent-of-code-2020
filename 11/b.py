
from copy import deepcopy

mat = [ ['.']+list(x)+['.'] for x in open('input').read().replace('L','#').splitlines() ] #
null = [ '.' for x in range(len(mat[0])) ]
# cmat = [null] + [ ['.']+[ '0' for y in range(len(mat[0])-2) ]+['.'] for x in mat ] + [null] #cmat is the number of # according to the rule, in matrix form.
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
        if y-j_d in d and bottom:
            cell = mat[y-j_d][i]
            if cell == 'L':
                bottom = False
            elif cell == '#':
                bottom = False
                c += 1
        if side:
            if mat[y][i] == "L":
                side = False
            if mat[y][i] == "#":
                side = False
                c += 1
        if c == 3: break
        j_d += 1
    return c

def RTX_top(r, i, mat):
    for j in r:
        if mat[j][i] == 'L':
            return 0
        elif mat[j][i] == '#':
            return 1
    return 0

dim_j = len(mat)-1
dim_i = len(mat[0])-1

domVERT = range(1,dim_j+1)  #Domain for vertical / j values
def RTX_ON(mat):
    mat_ = deepcopy(mat)
    d = False
    for x in range(1, dim_i):
        for y in range(1, dim_j):
            rN = range(y-1,0,-1)
            rS = range(y+1,dim_j+1)

            rE = range(x+1, dim_i+1)
            rW = range(x-1, 0, -1)

            c = (RTX_side(rE, domVERT, y, mat) + RTX_side(rW, domVERT, y, mat) + RTX_top(rN, x, mat) + RTX_top(rS, x, mat))
            # cmat[y][x] = (str)(c) #cmat is the number of # according to the rule, in matrix form.
            if mat[y][x] == '#' and c > 4:
                mat_[y][x] = 'L'
                d = True
            elif mat[y][x] == 'L' and c == 0:
                mat_[y][x] = '#'
                d = True
    if d == True:
        #print(""); [ print(x) for x in mat ]; print(""); [ print(x) for x in cmat ]; print(""); [ print(x) for x in mat_ ]; print("") #good ol' print debugging
        mat = RTX_ON(mat_)
        return mat
    return mat


simulated = RTX_ON(mat) #This is slow AF

[ print(''.join(x)) for x in simulated ] #output ascii, why not?
print(sum([ x.count('#') for x in simulated ]))
