import datetime
import itertools

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

with open("input/day_4.txt") as input:
    lines = []
    for line in input:
        lines.append(line[:-1])
    lines.sort()
    records = {}
    guard_id = 0
    for line in lines:
        time = datetime.datetime.strptime(line[1:17], "%Y-%m-%d %H:%S")
        if line[19] == "G":
            guard_id = int(line.split()[3][1:])
            if guard_id not in records:
                records[guard_id] = []
        else:
            records[guard_id].append(line)
    minutes = {}
    max_guard = -1
    max_sleep = -1
    for guard_id, record in records.items():
        minutes[guard_id] = [0 for _ in range(60)]
        minutes_sleeping = 0
        for asleep, awake in grouper(record, 2):
            asleep_start = int(asleep[15:17])
            awake_start = int(awake[15:17])
            for minute in range(asleep_start, awake_start):
                minutes[guard_id][minute] += 1
            minutes_sleeping += awake_start - asleep_start
        if minutes_sleeping >= max_sleep:
            max_guard = guard_id
            max_sleep = minutes_sleeping
    print(max_guard * minutes[max_guard].index(max(minutes[max_guard])))
