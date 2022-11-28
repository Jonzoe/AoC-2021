with open("AoC Day 2/Day2P1.txt") as file:
    data = [i for i in file.read().strip().split("\n")]

#print(data)

def movement():
    horizontal = 0
    depth = 0

    for count in data:
        word = count[:-2]
        place = int(count[-1])

        if word == 'forward':
            horizontal += place
        elif word == 'down':
            depth += place
        elif word == 'up':
            depth -= place

    return horizontal * depth

print("Svar: ",movement())