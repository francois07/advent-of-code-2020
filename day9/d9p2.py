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


def find_set(data, number):
    res = [0, 1]
    i = 0
    while i < len(data):
        set = data[res[0]:res[1]]
        add = sum(set)
        if add == number and number not in set:
            return set
        if add > number:
            i = res[0]+1
            res = [i, i+1]
            continue
        i += 1
        res[1] = i


n = find_set(input, find_nonsum(input, 25))
print(min(n)+max(n))
