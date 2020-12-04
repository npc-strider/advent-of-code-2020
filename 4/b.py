lines = open('input').read().splitlines()

arr = []
arr_ = []
for line in lines:
    _ = line.split(' ')
    if _[0] == '':
        arr.append(arr_)
        arr_ = []
    else:
        arr_ = arr_ + _
arr.append(arr_)

def v(v, k, l, u):
    if v[0] == k and l <= int(v[1]) <= u:
        return 1
    else:
        return 0

A = 0
for line in arr:
    c = 0
    print(line)
    for field in line:
        a = field.split(':')
        # if a[0] in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        #     c += 1
        c += v(a, 'byr', 1920, 2002)
        c += v(a, 'iyr', 2010, 2020)
        c += v(a, 'eyr', 2020, 2030)
        if a[0] == 'hgt':
            if a[1][-2]+a[1][-1] == 'cm' and 150 <= int(a[1].replace('cm', '')) <= 193:
                c += 1
            elif a[1][-2]+a[1][-1] == 'in' and 59 <= int(a[1].replace('in', '')) <= 76:
                c += 1
        elif a[0] == 'hcl' and a[1][0] == "#" and len(a[1]) == 7:
            c += 1
        elif a[0] == 'ecl' and a[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            c += 1
        elif a[0] == 'pid' and len(a[1]) == 9:
            c += 1
    print(c)
    if c == 7:
        A += 1

print(A)