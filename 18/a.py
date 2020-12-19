
import ast
import math

exprs = open('input').read().splitlines()

def specialeval(expr):
    expr_arr = ('+ '+expr).replace('(', '( + ').replace(')', ' ) ').split(' ')
    stack = [0]
    opstack = []
    level = 0
    # print(expr_arr)
    for i in range(0,len(expr_arr)-1,2):
        # print(stack)
        # print([expr_arr[i], expr_arr[i+1]])
        op = expr_arr[i]
        if expr_arr[i+1] == '(':
            level += 1
            stack.append(0)
            opstack.append(expr_arr[i])
        else:
            # print(expr_arr[i+1])
            if op == '+':
                stack[level] += int(expr_arr[i+1])
            elif op == '*':
                stack[level] *= int(expr_arr[i+1])
            else: # )
                op = opstack[level-1]
                if op == '+':
                    stack[level-1] += int(stack[level])
                elif op == '*':
                    stack[level-1] *= int(stack[level]) 
                level -= 1
                stack.pop()
                opstack.pop()
    return stack[0]

def a(exprs):
    return sum([specialeval(expr) for expr in exprs])

def b(exprs):
    return sum([
        specialeval('('+(expr+' * 1').replace('(','((').replace(')','))').replace(' * ', ') * (')+')')
        for expr in exprs
    ])

print(a(exprs))
print(b(exprs))