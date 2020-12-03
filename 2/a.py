lines = open("input").read().splitlines()

count = 0
for line in lines:
    line = line.replace('-',' ').replace(':','').split(' ')
    # print(line)
    # print(line[3].count(line[2]))
    if int(line[0]) <= line[3].count(line[2]) <= int(line[1]):
        count = count + 1

print(count)