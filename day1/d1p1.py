input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def find_pair(data, sum=2020):
    res = -1
    for i in data:
        for j in data:
            if i+j == sum:
                res = i*j
    return res


print(find_pair(input))
