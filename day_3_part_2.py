with open("input/day_3.txt") as input:
    inches = {}
    ids = []
    for line in input:
        params = line.split()
        cover_id = params[0]
        ids.append(cover_id)
        coords = params[2].split(',')
        left = int(coords[0])
        top = int(coords[1][:-1])
        dims = params[3].split('x')
        width = int(dims[0])
        height = int(dims[1])
        for row in range(left,left+width):
            for col in range(top,top+height):
                if (row,col) in inches:
                    inches[(row,col)].append(cover_id)
                else:
                    inches[(row,col)] = [cover_id]
    for clashes in inches.values():
        if len(clashes) > 1:
            for clash in clashes:
                    if clash in ids:
                        ids.remove(clash)
    print(ids)
