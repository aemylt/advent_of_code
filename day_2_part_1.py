with open('input/day_2.txt') as ids:
    twos = 0
    threes = 0
    for box_id in ids:
        letters = {}
        for letter in box_id:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        if 2 in letters.values():
            twos += 1
        if 3 in letters.values():
            threes += 1
    print(twos * threes)
