lines = open("data.txt").read().splitlines()

for u in lines:
    for v in lines:
        if int(u)+int(v) == 2020:
            print(int(u)*int(v))