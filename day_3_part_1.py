with open("input/day_3.txt") as input:
    inches = {}
    for line in input:
        params = line.split()
        coords = params[2].split(',')
        left = int(coords[0])
        top = int(coords[1][:-1])
        dims = params[3].split('x')
        width = int(dims[0])
        height = int(dims[1])
        for row in range(left,left+width):
            for col in range(top,top+height):
                if (row,col) in inches:
                    inches[(row,col)] += 1
                else:
                    inches[(row,col)] = 1
    print(len([inch for inch in inches.values() if inch > 1]))
