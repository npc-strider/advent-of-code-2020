import math

d = [ x.split(',') for x in open('input').read().splitlines() ]

def a(d):    #To be honest, I could've done this way quicker manually and got on the leaderboard. Formula is x - ID mod x for the waiting time
    x = int(d[0][0])
    ids = [ int(x) for x in d[1] if x != 'x' ] 
    delta = { id:(id - (x % id)) for id in ids if ( x := int(d[0][0]) )}
    minId = min(delta, key=delta.get)
    return (delta[minId]*minId)

print(a(d))

def b(d):
    d = [ ',(t+'+str(y)+')mod'+str(d[y])+'=0' for y in {i:d[i] for i in range(len(d))} if d[y] != 'x']
    return ''.join(d)[1:]


# I'm a math noob, so I just saw what everyone else is talking about and found this chinese remainder theorem.
# Why does this work? I DONT KNOW.
# I'll probably learn this when I get some formal CS education, so for now I'm just giving myself a rest for this part.
# Used a solver for that.

# x = 760171380521445
# x ≡ 0 mod 17 => x = n*17+0
# x ≡ −7 mod 41 => x = n*41-7 ???   # -7 because of 
# x ≡ −17 mod 643
# x ≡ −25 mod 23
# x ≡ −30 mod 13
# x ≡ −46 mod 29
# x ≡ −48 mod 433
# x ≡ −54 mod 37
# x ≡ −67 mod 19
 
print(b(d[1]))
