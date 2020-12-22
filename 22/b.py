from copy import deepcopy
players = {}
players.update({1:[ int(x) for x in open('input1').read().splitlines()[::-1]]})
players.update({2:[ int(x) for x in open('input2').read().splitlines()[::-1]]})

#print(players)

def recurse(decks,game):
    #print('game',game)
    #print(decks)
    previous_decks = {1:set(), 2:set()}
    i=0
    while True:
        i+=1

        if len(decks[1]) == 0:
            return [decks,False,True]
        elif len(decks[2]) == 0:
            return [decks,True,False]
            
        deck_str = {
            1: ' '.join([ str(x) for x in decks[1]]),
            2: ' '.join([ str(x) for x in decks[2]])
        }
        if deck_str[1] in previous_decks[1]:
            #print('BREAK: loop')
            #print(previous_decks, deck_str[1])
            decks[1].insert(0,decks[1].pop())
            decks[1].insert(0,decks[2].pop())
            return [decks,True,False]
        elif deck_str[2] in previous_decks[2]: #Ohh, it's ALWAYS player 1 that wins in this scenario..........................
            #print('BREAK: loop')
            #print(previous_decks, deck_str[2])
            decks[2].insert(0,decks[2].pop())
            decks[2].insert(0,decks[1].pop())
            return [decks,True,False]
        previous_decks[1].add(deck_str[1])
        previous_decks[2].add(deck_str[2])

        #print(decks)
        p1_top = decks[1].pop()
        p2_top = decks[2].pop()
        #print(i,p1_top,p2_top, p1_top > p2_top)

        if len(decks[1]) >= p1_top and len(decks[2]) >= p2_top:
            # print(decks)
            newdeck = {
                1:deepcopy((decks[1][-p1_top:])),
                2:deepcopy((decks[2][-p2_top:]))
            }
            # print('new',p1_top,p2_top,newdeck)
            data = recurse(newdeck,game+1)
            #print('back to game '+str(game))
            if data[1] == True: #=> Winner is p1
                #print('Winner p1')
                decks[1].insert(0,p1_top)
                decks[1].insert(0,p2_top)
            elif data[2] == True:
                #print('Winner p2')
                decks[2].insert(0,p2_top)
                decks[2].insert(0,p1_top)
            #print(decks)

        else:
            if p1_top > p2_top:
                decks[1].insert(0,p1_top)
                decks[1].insert(0,p2_top)
            else:
                decks[2].insert(0,p2_top)
                decks[2].insert(0,p1_top)

players = (recurse(players,1))[0]

i=1
c=0
print(players)
for x in players[1]:
    c+=(x*i)
    i+=1
print(c)
# between 33372 and 31653??
i=1
c=0
for x in players[2]:
    c+=(x*i)
    i+=1
print(c)