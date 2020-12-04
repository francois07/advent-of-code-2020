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


def check_multiple_slopes(data, slopes):
    return [check_slope(data, slope) for slope in slopes]


res = check_multiple_slopes(input, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
n = 1
for i in res:
    n *= i
print(n)
