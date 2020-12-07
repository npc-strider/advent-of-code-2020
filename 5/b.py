import math as m

lines = open('input').read().splitlines()

def uphalf(t):
    return [t[0], t[1] + int(abs(t[0] - t[1])/2) + 1]
def lowhalf(t):
    return [t[0] - int(abs(t[0] - t[1])/2) - 1, t[1]]

def bsp(dom, low, up, input):
    for p in input:
        if p == low:
            dom = lowhalf(dom)
        else:
            dom = uphalf(dom)
    if input[-1] == low:
        return dom[1]
    else:
        return dom[0]

ids = []
seats = []
rowdomain = [127, 0]
coldomain = [7, 0]

for line in lines:
    bruh = [
        bsp(rowdomain, "F", "B", line[0:7]),
        bsp(coldomain, "L", "R", line[7:10])
    ]
    id = bruh[0]*8 + bruh[1]
    ids.append(id)
    seats.append([bruh[0], bruh[1],id])

for i in range(0,128):
    for j in range(0,8):
        if i*8+j not in ids and i*8+j+1 in ids and i*8+j-1 in ids:
            print(i*8+j)