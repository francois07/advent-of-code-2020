input = [x for x in open('input.txt', 'r').read().splitlines()]


def check_position(data, x, y):
    return data[y][x % len(data[0])] == '#'


def check_slope(data, slope):
    height = len(data)
    n = 0
    for i in range(height):
        if slope[1]*i > height:
            break
        if check_position(data, slope[0]*i, slope[1]*i):
            n += 1
    return n


print(check_slope(input, (3, 1)))
