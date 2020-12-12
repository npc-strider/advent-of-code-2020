
# I love <3 complex numbers :3

import math

commands = [ [x[0],int(x[1:])] for x in open('input').read().splitlines()]

def pvec(d, m):
    return {
        'N' : complex(0,m),
        'E' : complex(m,0),
        'S' : complex(0,-m),
        'W' : complex(-m,0)
    }[d]

def a(commands):
    fv = 0+0j
    phase = 0
    for v in commands:
        d = v[0]
        m = v[1]
        if d == 'F':
            fv += (m*(1j)**(phase/90))
        elif d in ['L', 'R']:
            phase += {
                'L' : m,
                'R' : -m
            }[d]
        else:
            fv += pvec(d, m)
    return (int)(abs(fv.real) + abs(fv.imag))

print(a(commands))

def b(commands):
    fv = 0+0j
    wv = 10+1j
    for v in commands:
        d = v[0]
        m = v[1]
        if d == 'F':
            fv += m*wv
        elif d in ['L', 'R']:
            wv *= {
                'L' : (1j)**(m/90),
                'R' : (-1j)**(m/90)
            }[d]
        else:
            wv += pvec(d, m)
    return (int)(abs(fv.real) + abs(fv.imag))

print(b(commands))