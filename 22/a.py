
players = {}
players.update({1:[ int(x) for x in open('input1').read().splitlines()[::-1]]})
players.update({2:[ int(x) for x in open('input2').read().splitlines()[::-1]]})

print(players)
i=0
while True:
    i+=1
    if len(players[1]) > 0 and len(players[2]) > 0:
        p1_top = players[1].pop()
        p2_top = players[2].pop()
        # print(i,p1_top,p2_top, p1_top > p2_top)
        if p1_top > p2_top:
            players[1].insert(0,p1_top)
            players[1].insert(0,p2_top)
        elif p1_top < p2_top:
            players[2].insert(0,p2_top)
            players[2].insert(0,p1_top)
        # print(players[1])
        # print(players[2])
        # break
    else:
        break

i=1
c=0
for x in players[1]:
    c+=(x*i)
    i+=1
print(c)
i=1
c=0
for x in players[2]:
    c+=(x*i)
    i+=1
print(c)