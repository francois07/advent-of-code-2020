import numpy as np

input = [list(x) for x in open('input.txt', 'r').read().splitlines()]


def count_adjacent_occupied(data, x, y):
    res = 0
    found = []
    for i in range(1, len(data)):
        coords = [(y-i, x), (y, x+i), (y+i, x), (y, x-i),
                  (y-i, x+i), (y-i, x-i), (y+i, x-i), (y+i, x+i)]
        step = []
        for i, c in enumerate(coords):
            if (0 <= c[0] < len(data)) and (0 <= c[1] < len(data[0])) and i not in found:
                if data[c[0]][c[1]] == "#":
                    found.append(i)
                step.append(data[c[0]][c[1]])
        res += step.count("#")
    return res


def empty_rule(data):
    res = []
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                if count_adjacent_occupied(data, j, i) == 0:
                    res.append((i, j))
    return res


def occupied_rule(data):
    res = []
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == '#':
                if count_adjacent_occupied(data, j, i) >= 5:
                    res.append((i, j))
    return res


def apply_rules(data):
    new_grid = [row[:] for row in data]
    new_occupied = empty_rule(new_grid)
    new_empty = occupied_rule(new_grid)

    for coord in new_occupied:
        new_grid[coord[0]][coord[1]] = "#"
    for coord in new_empty:
        new_grid[coord[0]][coord[1]] = "L"

    return new_grid


def until_no_change(data):
    tmp = [row[:] for row in data]
    applied = apply_rules(tmp)
    i = 1
    while applied != tmp:
        tmp = applied
        applied = apply_rules(tmp)
        if applied == tmp:
            break
        i += 1
    return (i, applied)


n = until_no_change(input)
print(n[0])
print(sum([row.count("#") for row in n[1]]))
