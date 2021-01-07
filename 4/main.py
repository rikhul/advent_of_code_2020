import re

req = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

def valid(passport):
    for r in req:
        if r not in passport:
            return False
    return True

passport = ""
passports = []
for l in open("input.txt"):
    if l == "\n":
        passports.append(passport)
        passport = ""
    else:
        passport += (" " + l.strip())
passports.append(passport)

num_valid = 0
for p in passports:
    if valid(p):
        num_valid += 1

print(num_valid)


def byr(p):
    #(Birth Year) - four digits; at least 1920 and at most 2002.
    m = re.search(r"byr:(\d{4})([ \n]|$)", p)
    if not m:
        return False
    return 1920 <= int(m.group(1)) <= 2002


def iyr(p):
    #(Issue Year) - four digits; at least 2010 and at most 2020.
    m = re.search(r"iyr:(\d{4})([ \n]|$)", p)
    if not m:
        return False
    return 2010 <= int(m.group(1)) <= 2020

def eyr(p):
    # (Expiration Year) - four digits; at least 2020 and at most 2030.
    m = re.search(r"eyr:(\d{4})([ \n]|$)", p)
    if not m:
        return False
    return 2020 <= int(m.group(1)) <= 2030


def hgt(p):
    # (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    m = re.search(r"hgt:(\d+)(cm|in)([ \n]|$)", p)
    if not m:
        return False
    if m.group(2) == "cm":
        return 150 <= int(m.group(1)) <= 193
    if m.group(2) == "in":
        return 59 <= int(m.group(1)) <= 76
    return False

def hcl(p):
    # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return re.search(r"hcl:#[0-9a-f]{6}([ \n]|$)", p)

def ecl(p):
    # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)([ \n]|$)", p)

def pid(p):
    # (Passport ID) - a nine-digit number, including leading zeroes.
    return re.search(r"pid:\d{9}([ \n]|$)", p)

rules = (byr, iyr, eyr, hgt, hcl, ecl, pid)
def valid2(p):
    for r in rules:
        if not r(p):
            return False
    return True

num_valid2 = 0
for p in passports:
    if valid2(p):
        num_valid2 += 1
print(num_valid2)
