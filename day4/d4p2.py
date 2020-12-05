import re

input = [x for x in open('input.txt', 'r').read().split("\n\n")]

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_rules(field, data, colors=COLORS):
    if field == 'byr':
        return 1920 <= int(data) <= 2002
    elif field == 'iyr':
        return 2010 <= int(data) <= 2020
    elif field == 'eyr':
        return 2020 <= int(data) <= 2030
    elif field == 'hgt':
        return re.compile(r'^((59|6\d|7[0-6])in)|((1[5-8]\d|19[0-3])cm)$').match(data)
    elif field == 'hcl':
        return re.compile(r"^#[0-9a-f]{6}$").match(data)
    elif field == "ecl":
        return data in colors
    elif field == "pid":
        return re.compile(r'^\d{9}$').match(data)
    else:
        return False


def parse_fields(data):
    fields = re.split(r'\s|\n', re.sub(r'\n(?!.)', '', data))
    passport = {field.split(":")[0]: field.split(":")[1]
                for field in fields}
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


n = [check_passport(passport, optional=["cid"])
     for passport in input].count(True)
print(n)
