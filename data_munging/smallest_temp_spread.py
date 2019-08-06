import sys
def smallest(filename):
    smallest_change_day = -1
    smallest_change = sys.maxint
    lines = csv.reader(open(filename), delimiter=' ')
    next(lines)
    for line in lines:
        line = filter(lambda l: l == ' ', line)
        if  len(line) == 0:
            continue

        day = int(line[0])
        max_temp = float(line[1])
        min_temp = float(line[2])

        if max_temp - min_temp < smallest_change:
            smallest_change_day = day
            smallest_change = max_temp - min_temp 

    return smallest_change_day
