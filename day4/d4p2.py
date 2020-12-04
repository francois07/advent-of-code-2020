import re

input = [x for x in open('input.txt', 'r').read().split("\n\n")]

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_year(year, x, y):
    return len(year) == 4 and (x <= int(year) <= y)


def check_height(height, x_cm, y_cm, x_in, y_in):
    unit = height[-2:]
    measure = height[:-2]
    if unit == 'cm':
        return (x_cm <= int(measure) <= y_cm)
    elif unit == 'in':
        return (x_in <= int(measure) <= y_in)
    else:
        return False


def check_hex(hexa):
    value = hexa[1:]
    if hexa[0] != '#' or len(hexa) != 7:
        return False
    for char in value:
        if not (0 <= int(char, base=16) < 16):
            return False
    return True


def check_color(color, colors=COLORS):
    return color in colors


def check_rules(field, data):
    if field == 'byr':
        return check_year(data, 1920, 2002)
    elif field == 'iyr':
        return check_year(data, 2010, 2020)
    elif field == 'eyr':
        return check_year(data, 2020, 2030)
    elif field == 'hgt':
        return check_height(data, 150, 193, 59, 76)
    elif field == 'hcl':
        return check_hex(data)
    elif field == "ecl":
        return data in colors
    elif field == "pid":
        return len(data) == 9 and data.isnumeric()
    else:
        return False


def parse_fields(data):
    fields = re.split(r'\s|"\n"', data)
    passport = {field.split(":")[0]: field.split(":")[1]
                for field in fields if ':' in field}
    return passport


def check_passport(data, fields=FIELDS, optional=[]):
    passport = parse_fields(data)
    for field in fields:
        if field not in optional:
            if field not in passport:
                return False
            else:
                if not check_rules(field, passport[field]):
                    return False
    return True


i = 0
for passport in input:
    if check_passport(passport, optional=["cid"]):
        i += 1
print(i)
