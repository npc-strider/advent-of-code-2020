lines = open('input').read().splitlines()

arr = []
arr_ = []
for line in lines:
    _ = line.replace(':',' ').split(' ')
    if _[0] == '':
        arr.append(arr_)
        print("A")
        arr_ = []
    else:
        arr_ = arr_ + _
arr.append(arr_)

a = 0
for line in arr:
    print(line)
    c = 0
    for key in line:
        if key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            c += 1
    if c >= 7:
        a += 1
    print(c)

print(a)