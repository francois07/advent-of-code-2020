input = [list(x) for x in open('input.txt', 'r').read().splitlines()]


def occupied_adjacent(data, x, y, direction):
    for i in range(1, len(data)):
        dx = x+direction[1]*i
        dy = y+direction[0]*i
        if 0 <= dy < len(data) and 0 <= dx < len(data[0]):
            seat = data[dy][dx]
            if seat == "#":
                return True
            elif seat == "L":
                return False
        else:
            return False


def count_adjacent_occupied(data, x, y):
    coords = [(-1, 0), (0, 1), (1, 0), (0, -1),
              (-1, 1), (-1, -1), (1, -1), (1, 1)]
    res = [occupied_adjacent(data, x, y, (i, j))
           for i, j in coords].count(True)
    return res


def rule_coords(data):
    res = {
        "L": [],
        "#": []
    }
    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                if count_adjacent_occupied(data, j, i) == 0:
                    res["#"].append((i, j))
            if seat == "#":
                if count_adjacent_occupied(data, j, i) >= 5:
                    res["L"].append((i, j))
    return res


def apply_rules(data):
    new_grid = [row[:] for row in data]
    coords = rule_coords(new_grid)

    for i, j in coords["#"]:
        new_grid[i][j] = "#"
    for i, j in coords["L"]:
        new_grid[i][j] = "L"

    return new_grid


def until_no_change(data):
    grid = [row[:] for row in data]
    i = 0
    while apply_rules(grid) != grid:
        grid = apply_rules(grid)
        i += 1
    return (i, sum([row.count("#") for row in grid]))


n = until_no_change(input)
print(n)
