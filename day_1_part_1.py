with open("input/day_1.txt") as data:
    shift = sum([int(line) for line in data])
    print(shift)