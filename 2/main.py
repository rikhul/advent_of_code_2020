num_valid = 0
for l in open("input.txt"):
    rule, letter, pwd = l.split(" ")
    lower, upper = rule.split("-")
    lower, upper = int(lower), int(upper)
    letter = letter.strip(":")

    actual = pwd.count(letter)
    if lower <= actual <= upper:
        num_valid += 1

print(num_valid)

num_valid = 0
for l in open("input.txt"):
    rule, letter, pwd = l.split(" ")
    lower, upper = rule.split("-")
    lower, upper = int(lower), int(upper)
    letter = letter.strip(":")
    
    if (pwd[lower-1] == letter) ^ (pwd[upper-1] == letter):
        num_valid += 1

print(num_valid)
