from functools import lru_cache

input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def find_choices(data, jolts):
    return [x for x in data if 0 < (x-jolts) <= 3]


@lru_cache
def count_contained_recursive(outlet, data):
    n = 0
    for adapter in find_choices(data, outlet):
        n += count_contained_recursive(adapter, data)
    if outlet == max(data):
        return 1
    else:
        return n


print(count_contained_recursive(0, tuple(input)))
