shifts = {0:1}
shift = 0
while 2 not in shifts.values():
    with open("input/day_1.txt") as data:
        for line in data:
            shift += int(line)
            if shift in shifts:
                print(shift)
                shifts[shift] += 1
                break
            else:
                shifts[shift] = 1
