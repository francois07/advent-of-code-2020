input = [list(x) for x in open('input.txt', 'r').read().splitlines()]


def find_adjacent(data, x, y):
    coords = [(y-1, x), (y, x+1), (y+1, x), (y, x-1),
              (y-1, x+1), (y-1, x-1), (y+1, x-1), (y+1, x+1)]
    res = [data[c[0]][c[1]] for c in coords if (
        0 <= c[0] < len(data)) and (0 <= c[1] < len(data[0]))]
    return res


def empty_rule(data):
    res = []
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                if find_adjacent(data, j, i).count("#") == 0:
                    res.append((i, j))
    return res


def occupied_rule(data):
    res = []
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == '#':
                if find_adjacent(data, j, i).count("#") >= 4:
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
