with open("AoC Day 1/Day1.txt") as file:
    data = [int(i) for i in file.read().strip().split("\n")]
    
#def part1():
#Gjorde denna i Excel för hiskeligt länge sedan

def part2():
    allsum = [sum(total) for total in zip(data, data[1:], data[2:])]
    result = [allsum < secondsum for allsum, secondsum in zip(allsum, allsum[1:])]

    return sum(result)

print("Did part 1 in Excel")
print("Svar: ", part2())