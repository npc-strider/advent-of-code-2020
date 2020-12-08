
ACC = 0
INDEX = 0

indices = []

lines = [ [y[0],int(y[1])] for x in open('input').read().splitlines() if (y := x.split(' ')) ]

while INDEX not in indices:
    instruction = lines[INDEX][0]
    arg0 = lines[INDEX][1]
    print(instruction + '       ' + str(arg0) + '       ' + str(ACC) + '        ' + str(INDEX) )
    if instruction == 'nop':
        True
    elif instruction == 'acc':
        ACC += arg0
    elif instruction == 'jmp':
        INDEX += arg0 - 1
    indices.append(INDEX)
    INDEX += 1

    