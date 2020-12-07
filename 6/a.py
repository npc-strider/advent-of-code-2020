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
    s = []
    for p in group:
        s = s+p
    # print(group)
    # print(s)
    c += len(set(s))
print(c)