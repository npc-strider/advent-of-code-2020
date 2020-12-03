
lines = open('input').read().splitlines()
period = 31 #in chars

mat = []
for line in lines:
    mat_row = [1 if x == '#' else 0 for x in list(line)]
    mat.append(mat_row)

count = 0
j_ = 0
for i in range(0, len(mat)):
    print(mat[i])
    j = j_ % period
    j_ += 3
    
    if (mat[i][j] == 1):
        count += 1
print(count)