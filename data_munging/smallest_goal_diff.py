import csv
import sys

def smallest_goal(filename):
    f = open(filename)
    lines = csv.reader(open(filename), delimiter=' ')
    next(lines)
    smallest_diff = sys.maxsize
    smallest_name = None
    for line in lines:
        line = list(filter(lambda l: l != '', line))
        if len(line) < 10:
            continue

        diff = abs(int(line[6]) - int(line[8]))
        if diff < smallest_diff:
            smallest_diff = diff
            smallest_name = line[1]

    return "{} {}".format(smallest_name, str(smallest_diff))
