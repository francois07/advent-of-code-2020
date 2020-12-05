import re

input = [x for x in open('input.txt', 'r').read().split("\n\n")]

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def parse_fields(data):
    fields = re.split(r'\s|\n', re.sub(r'\n(?!.)', '', data))
    passport = {field.split(":")[0]: field.split(":")[1]
                for field in fields}
    return passport


def check_passport(data, fields=FIELDS, optional=[]):
    passport = parse_fields(data)
    for field in fields:
        if field not in optional and field not in passport:
            return False
    return True


n = [check_passport(passport, optional=["cid"])
     for passport in input].count(True)
print(n)
