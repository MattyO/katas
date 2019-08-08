import sys
import csv
def smallest(filename):
    smallest_change_day = -1
    smallest_change = sys.maxsize
    f = open(filename)
    lines = csv.reader(open(filename), delimiter=' ')
    next(lines)
    for line in lines:
        line = list(filter(lambda l: l != '', line))
        if  len(line) == 0:
            continue

        day = line[0]
        try:
            max_temp = float(line[1].replace("*", ''))
            min_temp = float(line[2].replace("*", ''))
        except Exception as ex:
            print(ex)

        if max_temp - min_temp < smallest_change:
            smallest_change_day = day
            smallest_change = max_temp - min_temp 

    f.close()

    return smallest_change_day
