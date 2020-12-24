# This isn't working... knew something was wrong with just using basic +/-1 translations, you would expect something with irrational numbers by exressing a hex grid as a 2d vector (square grid)

# directions = [x.replace('e','e ').replace('w','w ')[:-1].split(' ') for x in open('input').read().splitlines()]

# D = {
#     'ne':   0+1j,
#     'se':   0-1j,
#     'sw':   -1-1j,
#     'nw':   -1+1j,
#     'e':    1+0j,
#     'w':    -1+0j
# }
# # print(directions)

# #So a bit of a problem: NWSW != N+S+W+W. So we need to use the identity NWSW = W, NESE = E, ...
# vectors = []
# for direction in directions:
#     count = {x:direction.count(x) for x in D }
#     vector = 0+0j
#     print(direction,count)
#     de = count['ne'] - count['se']
#     vector += min(count['ne'],count['se'])*D['e']
#     if de > 0:
#         vector += de*D['ne']
#     else:
#         vector += de*D['se']
#     dw = count['nw'] - count['sw']
#     vector += min(count['nw'],count['sw'])*D['w']
#     if dw > 0:
#         vector += dw*D['nw']
#     else:
#         vector += dw*D['sw']
#     vector += (count['e']*D['e'] + count['w']*D['w'])
#     # print(vector)
#     vectors.append(vector)
#     # vectors.append(sum([ D[x] for x in direction ]))

# print({x:vectors.count(x) for x in vectors})
# print()
# print({x:vectors.count(x) for x in vectors if (vectors.count(x)%2 == 1)}) #196 too low, 181 too low
# print(len([x for x in vectors if (vectors.count(x)%2 == 1)])) #196 too low, 181 too low