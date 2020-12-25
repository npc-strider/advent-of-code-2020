from operator import add, sub
from copy import deepcopy

directions = [x.replace('e','e ').replace('w','w ')[:-1].split(' ') for x in open('input').read().splitlines()]

def getHexAdjacent(vec):
    adj = {}
    di,dj,dk = (0,1,1)
    adj.update({
        'sw': (vec[0]+di,vec[1]+dj,vec[2]+dk),
        'ne': (vec[0]-di,vec[1]-dj,vec[2]-dk)
    })
    di,dj,dk = (1,-1,0)
    adj.update({
        'e': (vec[0]+di,vec[1]+dj,vec[2]+dk),
        'w': (vec[0]-di,vec[1]-dj,vec[2]-dk)
    })
    di,dj,dk = (1,0,1)
    adj.update({
        'se': (vec[0]+di,vec[1]+dj,vec[2]+dk),
        'nw': (vec[0]-di,vec[1]-dj,vec[2]-dk)
    })
    return adj

def toggle(boolean):
    return (False if boolean else True)

grid = {(0,0,0):{'state':False}}

vectors = []
for direction in directions:
    # print(direction)
    vec = (0,0,0)
    for dir_ in direction:
        vec = getHexAdjacent(vec)[dir_]
    grid.update({vec:{'state':toggle(grid[vec]['state'] if vec in grid else False)}})
    vectors.append(vec)

#Part 1
print(len([ x for x in grid if (grid[x]['state'] == True)])) # Black => True, white => false

#Part 2
grid_ = deepcopy(grid)  #expand our space by one hextile in each direction
for cell in grid:
    adj = getHexAdjacent(cell)
    for cell_ in adj:
        cell_ = adj[cell_]
        if cell_ not in grid:
            grid_.update({cell_:{'state':False}})

i = 0
while i < 100:
    grid = grid_
    grid_ = deepcopy(grid)
    for cell in grid:
        adj = getHexAdjacent(cell)
        c = 0
        for cell_ in adj:
            cell_ = adj[cell_]
            if cell_ in grid:
                if grid[cell_]['state'] == True:
                    c+=1
            else:
                grid_.update({cell_:{'state':False}})

        if grid[cell]['state'] == True and (c == 0 or c > 2):
            grid_[cell]['state'] = False
        elif grid[cell]['state'] == False and c == 2:
            grid_[cell]['state'] = True
    i+=1
print(len([ x for x in grid_ if (grid_[x]['state'] == True)]))
