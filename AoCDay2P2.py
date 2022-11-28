with open("AoC Day 2/Day2P2.txt") as file:
    data = [i for i in file.read().strip().split("\n")]
    print(data)

def movement():
    horizontal = 0
    depth = 0
    aim = 0

    for count in data:
        word = count[:-2]
        place = int(count[-1])

        if word == 'forward':
            horizontal += place
            depth += aim * place
        elif word == 'down':
            aim += place
        elif word == 'up':
            aim -= place

    return horizontal * depth

print("Svar: ",movement())