input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def has_pair(data, sum):
    for i in data:
        for j in data:
            if i+j == sum:
                return True
    return False


def find_nonsum(data, nb_previous):
    for i in range(nb_previous, len(data)):
        if not has_pair(data[i-nb_previous:i], data[i]):
            return data[i]
    return -1


print(find_nonsum(input, 25))
