import sys, re

REQUIRED = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

passports = sys.stdin.read().split("\n\n")

total = 0
for passport in passports:
    fields = re.findall('(\w+):[^\s]+', passport)
    total += (set(fields) & REQUIRED) == REQUIRED

print(total)