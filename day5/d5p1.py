input = [x for x in open('input.txt', 'r').read().splitlines()]


def get_1d_position(data, lower_letter="F", upper_letter="B", range=128):
    position = [0, range-1]
    for letter in data:
        if letter == lower_letter:
            position[1] -= ((position[1]-position[0])//2 +
                            (position[1]-position[0]) % 2)
        if letter == upper_letter:
            position[0] += ((position[1]-position[0])//2 +
                            (position[1]-position[0]) % 2)
        if position[0] == position[1]:
            break
    return position[0]


def get_2d_position(data):
    args = (data[:-3], data[-3:])
    row = get_1d_position(args[0])
    col = get_1d_position(args[1], "L", "R", range=8)
    return {
        "row": row,
        "col": col,
        "id": (row*8 + col)
    }


n = max([get_2d_position(data)["id"] for data in input])
print(n)
