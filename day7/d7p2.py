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


def count_contained_recursive(color, parsed_rules):
    n = sum([int(bag[0]) for bag in parsed_rules[color]])
    for bag in parsed_rules[color]:
        n += count_contained_recursive(bag[1], parsed_rules) * int(bag[0])
    return n


parsed_rules = parse_rules(input)
print(count_contained_recursive("shiny gold", parsed_rules))
