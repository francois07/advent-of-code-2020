input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def find_triplet(data, sum=2020):
    res = -1
    for i in input:
        for j in input:
            for h in input:
                if i+j+h == 2020:
                    res = i*j*h
    return res


print(find_triplet(input))
