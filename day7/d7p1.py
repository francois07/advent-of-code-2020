import re

input = [x for x in open('input.txt', 'r').read().splitlines()]


def parse_rules(data):
    res = {}
    for rule in data:
        split = re.split(r' bags contain | bags, | bag,', rule)
        bag_color = split[0]
        contained_bags = []
        for contained in split[1:]:
            stripped = re.sub(r' bags\.| bag\.', '', contained)
            count = re.search(r'\d+', stripped)
            if count:
                color = re.sub(r'\d+', '', stripped).strip()
                contained_bags.append((count.group(), color))
        res[bag_color] = contained_bags
    return res


def find_containers(color, parsed_data):
    match = [x for x in parsed_data if len(
        [y for y in parsed_data[x] if y[1] == color]) >= 1]
    return match


def count_containers_recursive(color, parsed_data, x=[]):
    containers = find_containers(color, parsed_data)
    n = len([bag for bag in containers if bag not in x])
    [x.append(bag) for bag in containers]
    for color in containers:
        n += count_containers_recursive(color, parsed_data, x)
    return n


parsed_rules = parse_rules(input)
print(count_containers_recursive("shiny gold", parsed_rules))
