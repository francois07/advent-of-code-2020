input = [int(x) for x in open('input.txt', 'r').read().splitlines()]


def find_choices(data, jolts):
    return [x for x in data if 0 < (x-jolts) <= 3]


def use_all_adapters(data, outlet=0):
    jolts = outlet
    adapters = [outlet]
    while jolts < max(data)+3:
        choices = find_choices(data, jolts)
        if len(choices) > 0:
            adapter = min(choices)
        else:
            adapter = max(data)+3
        adapters.append(adapter)
        jolts = adapter
    return adapters


def count_differences(data, jolts):
    res = []
    for i in jolts:
        count = [i, [data[j] - data[j-1] ==
                     i for j in range(1, len(data))].count(True)]
        res.append(count)
    return res


n = count_differences(use_all_adapters(input), [1, 3])
print(n[0][1]*n[1][1])
