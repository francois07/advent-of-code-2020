input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def find_triplet(data, sum=2020):
    res = -1
    for i in data:
        for j in data:
            for h in data:
                if i+j+h == sum:
                    res = i*j*h
    return res


print(find_triplet(input))
