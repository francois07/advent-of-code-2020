input = [x for x in open('input.txt', 'r').read().splitlines()]


def get_id(data):
    binary = data.replace("B", "1").replace(
        "F", "0").replace("R", "1").replace("L", "0")
    return int(binary, 2)


n = max([get_id(data) for data in input])
print(n)
