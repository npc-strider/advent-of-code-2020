from copy import deepcopy
import itertools

foods = [ [ set(y.replace(',','').split(' ')) for y in x.replace(')','').split(' (contains ')] for x in open('input').read().splitlines() ]

recipes = [ x[0] for x in foods ]
allergens = [ x[1] for x in foods ]
# print(foods)
# print(recipes)
def get_relationships(values):
    relationships = {}
    for r in values:
        # print(r)
        for ig in r:
            if ig not in relationships:
                relationships.update({ig:set()})
                i=0
                for r_ in values:
                    if ig in r_:
                        relationships[ig].add(i)
                    i+=1
    return relationships
# print(get_relationships(recipes))
# print(get_relationships(allergens))

rel = get_relationships(recipes)
arel = get_relationships(allergens)
non_allergen = []
for i in rel:
    possible = False
    for a in arel:
        # print(rel[i].intersection(arel[a]))
        if len(rel[i].intersection(arel[a])) == len(arel[a]):
            possible = True
            break
    if possible == False:
        non_allergen.append(i)
    # print(possible, i)

c=0
for i in non_allergen:
    c+=list(itertools.chain(*recipes)).count(i)

print(c)


rel = get_relationships(recipes)
arel = get_relationships(allergens)
allergen = {}
for i in rel:
    test = []
    for a in arel:
        # print(rel[i].intersection(arel[a]))
        if len(rel[i].intersection(arel[a])) == len(arel[a]):
            test.append(a)
            
    if len(test) > 0 :
        allergen.update({i:test})
    # print(test, i)

# print(allergen)
sorted_list = {}
def alupdate(allergen):
    allergen_ = deepcopy(allergen)
    mod = False
    for al in allergen:
        als = allergen[al]
        if len(als) == 1:
            sorted_list.update({als[0]:al})
            for al_ in allergen:
                if als[0] in allergen[al_]:
                    _ = allergen_[al_]
                    _.remove(als[0])
                    allergen_[al_] = _
            mod = True
    # print(allergen_)
    if mod == True:
        alupdate(allergen_)
    else:
        for al in allergen_:
            if len(allergen_[al]) == 1:
                sorted_list.update({allergen_[al][0]:al})

alupdate(allergen)

# print(sorted_list)
print(','.join([sorted_list[x] for x in sorted(sorted_list)]))