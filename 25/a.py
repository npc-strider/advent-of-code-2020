
div = 20201227

card_public = 5764801
door_public = 17807724

def transform(subject,lpt):
    value = 1
    c = 0
    while c < lpt:
        value *= subject
        value = value % div
        # print(c, value)
        c+=1
    return value

def bruteforce(value_goal):
    lpt = 1
    value = 1
    while True:
        value *= 7
        value = value % div
        if value == value_goal:
            return lpt
        lpt += 1

card_lpt_size = bruteforce(card_public)
door_lpt_size = bruteforce(door_public)
print(card_lpt_size, door_lpt_size)
print(transform(door_public,card_lpt_size))