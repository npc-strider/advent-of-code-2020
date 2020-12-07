lines = open('input').read().replace(' bags','').replace(' bag','').replace('.','').splitlines()

empties = []
dictionary = {}
for line in lines:
    r = line.split(' contain ')
    if 'no other' in line or r[0] == 'shiny gold':
        dictionary[r[0]] = {}
        empties.append(r[0])
    else:
        dictionary[r[0]] = {y[1]: int(y[0]) for x in r[1].split(', ') if (y := x.split(' ',1))}
for i in range(1,10): #Ten because why not? Not breaking at the amount of passes I need for this
    for u in dictionary:
        # print(u)
        # print(dictionary[u])
        a = {}
        for v in dictionary[u]:
            k = dictionary[u][v]
            if v not in empties:
                a.update({x:y*k for x in dictionary[v] if (y := dictionary[v][x])})
            else:
                a.update({v:k})
        dictionary[u] = a

c = 0
for k in dictionary:
    if 'shiny gold' in dictionary[k].keys():
        c += 1
        print(k)
        print(dictionary[k]['shiny gold'])
print(c)