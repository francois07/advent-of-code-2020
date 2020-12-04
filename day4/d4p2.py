import re

input = [x for x in open('input.txt', 'r').read().split("\n\n")]

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_digits(data, n):
    if len(data) != n:
        return False
    else:
        return True


def check_between(data, x, y):
    n = int(data)
    if n < x or n > y:
        return False
    else:
        return True


def check_year(year, x, y):
    return check_digits(year, 4) and check_between(year, x, y)


def check_height(height, x_cm, y_cm, x_in, y_in):
    u = height[-2:]
    n = height[:-2]
    if u == 'cm':
        return check_between(n, x_cm, y_cm)
    if u == 'in':
        return check_between(n, x_in, y_in)


def check_hex(hexa):
    h = hexa[1:]
    if hexa[0] != '#' or not check_digits(hexa, 7):
        print(1)
        return False
    for l in h:
        if not 0 <= int(l, base=16) < 16:
            return False
    return True


def check_color(data, colors=COLORS):
    if data not in colors:
        return False
    else:
        return True


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
        return check_color(data)
    elif field == "pid":
        return check_digits(data, 9)


def parse_fields(data):
    fields = re.split(r'\s|"\n"', data)
    passport = {field.split(":")[0]: field.split(":")[1]
                for field in fields if field != ''}
    return passport


def check_passport(data, fields=FIELDS, optional=[]):
    passport = parse_fields(data)
    for field in fields:
        if field not in optional and field not in passport:
            return False
        elif field in passport and field not in optional:
            if not check_rules(field, passport[field]):
                return False
    return True


n = 0
for passport in input:
    if check_passport(passport, optional=["cid"]):
        n += 1
    else:
        print(passport+"\n---")
print(n)
