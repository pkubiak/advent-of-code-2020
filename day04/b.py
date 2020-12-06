import sys, re

VALIDATIONS = {
    'byr': lambda v: v.isdecimal() and 1920 <= int(v) <= 2002,
    'iyr': lambda v: v.isdecimal() and 2010 <= int(v) <= 2020,
    'eyr': lambda v: v.isdecimal() and 2020 <= int(v) <= 2030,
    'hgt': lambda v: v[:-2].isdecimal() and ('in' in v and 59 <= int(v[:-2]) <= 76) or ('cm' in v and 150 <= int(v[:-2]) <= 193),
    'hcl': lambda v: re.fullmatch('#[0-9a-f]{6}', v),
    'ecl': lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda v: re.fullmatch('\d{9}', v),
}

passports = sys.stdin.read().split("\n\n")

total = 0
for passport in passports:
    fields = dict(re.findall('(\w+):([^\s]+)', passport))
    total += all(
        fn(fields.get(key,'')) 
        for key, fn in VALIDATIONS.items()
    )

print(total)