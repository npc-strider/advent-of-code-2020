import copy

instructions = [ [y[0],int(y[1])] for x in open('input').read().splitlines() if (y := x.split(' ')) ]

def interpreter(instructions):    
    ACC = 0
    INDEX = 0
    indices = []
    while True:
        if INDEX in indices:
            return False
        elif INDEX == len(instructions):
            return ACC
            # return True
        else:
            instruction = instructions[INDEX][0]
            arg0 = instructions[INDEX][1]
            # print(instruction + '       ' + str(arg0) + '       ' + str(ACC) + '        ' + str(INDEX) )
            if instruction == 'nop':
                True
            elif instruction == 'acc':
                ACC += arg0
            elif instruction == 'jmp':
                INDEX += arg0 - 1
            indices.append(INDEX)
            INDEX += 1

for i in range(0,len(instructions)):
    instructions_ = copy.deepcopy(instructions)
    instruction = instructions_[i][0]
    if instruction == 'jmp':
        instructions_[i][0] = 'nop'
        print('jmp -> nop   ' + str(i))
    elif instruction == 'nop' and instructions_[i][1] != 0:
        print('nop -> jmp   ' + str(i))
        instructions_[i][0] = 'jmp'
    
    c = interpreter(instructions_)
    if c != False:
        print(c) #758???
        break
