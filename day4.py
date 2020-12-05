#!/usr/bin/python3
import re
from pprint import pprint

def is_field_valid(field, value):
    if field == 'byr':
        return len(value) == 4 and 1920 <= int(value) and int(value) <= 2002
    elif field == 'iyr':
        return len(value) == 4 and 2010 <= int(value) and int(value) <= 2020
    elif field == 'eyr':
        return len(value) == 4 and 2020 <= int(value) and int(value) <= 2030
    elif field == 'hgt':
        try:
            unit = value[-2:]
            value = int(value[:-2])
        except:
            return False
        return ('cm' == unit and 150 <= value and value <= 193) or ('in' == unit and 59 <= value and value <= 76)
    elif field == 'hcl':
        return re.match(r'^#[a-f0-9]{6}$', value) is not None
    elif field == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field == 'pid':
        return value.isdigit() and len(value) == 9

def is_passport_valid(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in req_fields:
        if field not in passport or not is_field_valid(field, passport[field]):
            return False
    return True

def fst(passports):
    return sum([is_passport_valid(item) for item in passports])

if __name__ == '__main__':

    raw_list = open('/tmp/input.txt', 'r').read().splitlines()

    passports = []
    d = {}
    for line in raw_list:
        if line == '':
            passports.append(d)
            d = {}
        else:
            for arg in line.split():
                lst = arg.split(':')
                key, value = lst[0], ':'.join(lst[1:])
                d[key] = value
    passports.append(d)
    print(fst(passports))
