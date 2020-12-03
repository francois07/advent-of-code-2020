input = [x for x in open('input.txt', 'r').read().splitlines()]


def check_position(data, x, y):
    if data[y][x % len(data[0])] == '#':
        return 1
    else:
        return 0


def check_slope(data, slope):
    height = len(data)
    n = 0
    for i in range(height):
        if slope[1]*i > height:
            break
        n += check_position(data, slope[0]*i, slope[1]*i)
    return n


print(check_slope(input, (3, 1)))
