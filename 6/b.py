lines = open('input').read().splitlines()

arr = []
_ = []
for line in lines:
    if line == '':
        arr.append(_)
        _ = []
    else:
        _.append(list(line))
arr.append(_)

c = 0
for group in arr:
    s = set(group[0])
    print(group)
    for p in group:
        s = s & set(p)
    print(s)
    c += len(s)
print(c)