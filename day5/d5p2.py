input = [x for x in open('input.txt', 'r').read().splitlines()]


def get_id(data):
    binary = data.replace("B", "1").replace(
        "F", "0").replace("R", "1").replace("L", "0")
    return int(binary, 2)


def get_missing_seat(data):
    for id in data:
        if id+1 not in data and id+2 in data:
            return id+1
    return -1


n = get_missing_seat([get_id(data) for data in input])
print(n)
