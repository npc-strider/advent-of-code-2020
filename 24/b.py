directions = [x.replace('e','e ').replace('w','w ')[:-1].split(' ') for x in open('input').read().splitlines()]

import math
import cmath

def cround(z,n):
    return round(z.real, n)+1j*round(z.imag, n)

D = {
    'ne':   math.sqrt(5)*cmath.exp(1j*math.pi/3),
    'se':   math.sqrt(5)*cmath.exp(-1j*math.pi/3),
    'sw':   math.sqrt(5)*cmath.exp(-1j*2*math.pi/3),
    'nw':   math.sqrt(5)*cmath.exp(1j*2*math.pi/3),
    'e':    math.sqrt(5)+0j,
    'w':    -math.sqrt(5)+0j
}

vectors = []
for direction in directions:
    vectors.append(cround(sum([ D[x] for x in direction ]),6))

print(len([x for x in vectors if (vectors.count(x)%2 == 1)]))