
import re

# Fook the other solution attempt (a.py.OLD):
# I'm using grep -P now. - getting lazy.

rules = { rule[0]:'( '+rule[1].replace('"','')+' )' for x in open('input_rules').read().splitlines() if (rule := x.split(': ')) }
rules.update({i:rules[i].replace('( ','').replace(' )','') for i in rules if (rules[i] in ['( a )','( b )'])})
# print(rules)
def expand(rules,breaker): #You know the rules, and so do I
    mod = False
    for i in rules:
        rule = rules[i].split(' ')
        # print(rule)
        j = 0
        for k in rule:
            if k.isnumeric():
                mod = True
                rule[j] = rules[k]
            j += 1
        rules[i] = ''.join(rule)
    if mod and breaker < 4:
        breaker += 1
        rules = expand(rules, breaker)
    return rules
# print("grep -P '"+expand(rules)['0']+"' input")
print()
regxp = re.compile('^'+expand(rules,0)['0']+'$')
matched = [ x for x in open('input').read().splitlines() if (regxp.match(x))]
# [print(x)for x in matched]
print(len(matched))

