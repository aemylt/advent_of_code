with open('input/day_2.txt') as id_file:
    ids = []
    answer = ""
    for box_id in id_file:
        box_id = box_id[:-1]
        for prev_id in ids:
            matches = []
            for box_char, prev_char in zip(box_id, prev_id):
                if box_char == prev_char:
                    matches.append(box_char)
            if len(matches) == len(box_id) - 1:
                answer = "".join(matches)
                break
        if answer != "":
            break
        else:
            ids.append(box_id)
    print(answer)
