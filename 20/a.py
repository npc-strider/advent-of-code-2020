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

def get_edges_(tile,phase):
    if phase == 0:
        return [
            tile[0],
            ''.join([tile[j][-1] for j in range(len(tile))]),
            tile[-1],
            ''.join([tile[j][0] for j in range(len(tile))])
        ]
    elif phase == 90:
        return [
            ''.join([tile[j][0] for j in range(len(tile))]),
            tile[0],
            ''.join([tile[j][-1] for j in range(len(tile))]),
            tile[-1],
        ]
    elif phase == 180:
        return [
            tile[0][::-1],
            ''.join([tile[j][-1] for j in range(len(tile))])[::-1],
            tile[-1][::-1],
            ''.join([tile[j][0] for j in range(len(tile))])[::-1]
        ]
    else:
        return [
            ''.join([tile[j][-1] for j in range(len(tile))])[::-1],
            tile[-1][::-1],
            ''.join([tile[j][0] for j in range(len(tile))])[::-1],
            tile[0][::-1],
        ]

relationships = {} # <3
edges = { id:get_edges(tiles[id]) for id in tiles }
for id in edges:
    tile_edges = edges[id]
    relationships.update({id:[]})
    for id_ in edges:
        if id != id_:
            adj = list(tile_edges.intersection(edges[id_]))
            if len(adj) > 0:
                relationships[id].append(id_)
                print(adj[0], '=>', id, '->', id_)

print(math.prod([int(id) for id in relationships if (len(relationships[id]) == 2)]))

#Part 2!
relationships = {} # <3
edges = { id:get_edges(tiles[id]) for id in tiles }
for id in edges:
    tile_edges = edges[id]
    relationships.update({id:[]})
    for id_ in edges:
        if id != id_:
            adj = list(tile_edges.intersection(edges[id_]))
            if len(adj) > 0:
                relationships[id].append(id_)
                print(adj[0], '=>', id, '->', id_)
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
            # print(d-x, x, get_adj(x, d, idom, jdom, grid))
            adjacent = get_adj(x, d, idom, jdom, grid)
            adjacent_ = [ x for x in adjacent if (x != None) ]
            phase = 0
            if len(adjacent_) == 1:
                adj = {x:y for x in relationships[adjacent_[0]] if (y := relationships[x])}
                # print(adj)
                # print(set([ x for x in adj if (len(adj[x]) < 4)]).difference(done))
                add = set([ x for x in adj if (len(adj[x]) < 4)]).difference(done)
                add = list(add)[0]
                # add = relationships[adjacent_[0]][i]
                if adjacent[0] != None: # => Top
                    print( "AAAAAAAAAAAAAAAAAAAAAAAAAAA", adjacent[0])
                    print(tiles[adjacent[0]])
                else: #adjacent[1] => Left
                    print( "BBBBBBBBBBBBBBBBBBBBBBBB", adjacent[1])
                i+=1
            if len(adjacent_) == 2:
                add = set(relationships[adjacent_[0]]).intersection(set(relationships[adjacent_[1]])).difference(done)
                # print(add)
                add = list(add)[0]

            grid[d-x][x] = add
            done.add(add)
            # [print(grid[x]) for x in grid]
                # exit(-1)
            # i+=1
# grid[d][d+1] = rel[1]
# print(relationships[start])
[print(grid[x]) for x in grid]
print()
[print(phase_grid[x]) for x in phase_grid]