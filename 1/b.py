lines = open("data.txt").read().splitlines()

numbers = []

for u in lines:
    for v in lines:
        for w in lines:
            if int(u)+int(v)+int(w) == 2020:
                print(int(u)*int(v)*int(w))