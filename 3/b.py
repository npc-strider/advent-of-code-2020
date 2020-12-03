
lines = open('input').read().splitlines()
period = 31 #in chars

mat = []
for line in lines:
    mat_row = [1 if x == '#' else 0 for x in list(line)]
    mat.append(mat_row)


ld = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

lcount = []
for d in ld:
    dx = d[0]
    dy = d[1]
    j_ = 0
    count = 0
    for i in range(0, len(mat), dy):
        j = j_ % period
        j_ += dx
        
        if (mat[i][j] == 1):
            count += 1
    lcount.append(count)

print(lcount)
ans = 1
for r in lcount:
    ans = r*ans

print(ans)