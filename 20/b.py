import math
data = open('input').read().splitlines()

id = 0
tiles = {}
for line in data:
    if line[0:4] == 'Tile':
        id = line[5:9]
        tiles.update({id:[]})
    elif len(line) > 0:
        tiles[id].append(line)

def get_edges(tile):
    return {
        tile[0],
        ''.join([tile[j][-1] for j in range(len(tile))]),
        tile[-1],
        ''.join([tile[j][0] for j in range(len(tile))]),
        
        tile[0][::-1],
        ''.join([tile[j][-1] for j in range(len(tile))])[::-1],
        tile[-1][::-1],
        ''.join([tile[j][0] for j in range(len(tile))])[::-1]
    }

relationships = {} # <3
edges = { id:get_edges(tiles[id]) for id in tiles }
for id in edges:
    tile_edges = edges[id]
    relationships.update({id:[]})
    for id_ in edges:
        if id != id_:
            # print(tile_edges)
            adj = list(tile_edges.intersection(edges[id_]))
            if len(adj) > 0:
                relationships[id].append(id_)
                # print(adj[0], '=>', id, '->', id_)

start = [id for id in relationships if (len(relationships[id]) == 2)][0]
dim = 3
grid = {j:{i:None for i in range(dim)} for j in range(dim)}
phase_grid = {j:{i:None for i in range(dim)} for j in range(dim)}
d = 0

def get_adj(x, d, idom, jdom, grid):
    adj = [None, None]
    if d-x-1 in jdom:
        adj[0] = grid[d-x-1][x]
    if x-1 in idom:
        adj[1] = grid[d-x][x-1]
    return adj

for i in tiles:
    tiles[i] = [ list(x) for x in tiles[i] ]

done = set()

grid[0+d][d] = start
phase_grid[0][0] = 0
done.add(start)
idom = grid[0].keys()
jdom = grid.keys()
for d in range(1,50):
    i = 0
    for x in range(0,d+1):
        if d-x in jdom and x in idom:
            adjacent = get_adj(x, d, idom, jdom, grid)
            adjacent_ = [ x for x in adjacent if (x != None) ]
            phase = 0
            if len(adjacent_) == 1:
                adj = {x:y for x in relationships[adjacent_[0]] if (y := relationships[x])}
                add = set([ x for x in adj if (len(adj[x]) < 4)]).difference(done)
                add = list(add)[0]
                i+=1
            if len(adjacent_) == 2:
                add = set(relationships[adjacent_[0]]).intersection(set(relationships[adjacent_[1]])).difference(done)
                add = list(add)[0]

            grid[d-x][x] = add
            done.add(add)

[print(grid[x]) for x in grid]
print()
[print(phase_grid[x]) for x in phase_grid]


for i in range(1,3):
    print(''.join([ tiles[grid[0][i-1]][j][-1] for j in range(len(tiles[grid[0][i-1]])) ]))
    this_vertical = ''.join([ tiles[grid[0][i]][j][0] for j in range(len(tiles[grid[0][i]])) ])
    print(this_vertical)
    print(this_vertical[::-1])
    print()
