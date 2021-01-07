import re

pattern = re.compile(r"(.+) bags contain (.*)")
pattern2 = re.compile(r"(\d+) (.*?) bag[s]?")

bags = {}

for l in open("input"):
    res = pattern.search(l)
    color, contents = res.groups()
    res2 = pattern2.findall(res.groups()[1])
    bags[color] = dict((color, int(count)) for count, color in res2)

def contains(color, bags):
    possible_bags = set()
    for c, sub_colors in bags.items():
        if color in sub_colors.keys():
            possible_bags.add(c)
            possible_bags = possible_bags.union(contains(c, bags))
    return possible_bags

print(len(contains("shiny gold", bags)))

def total_bags(color, bags):
    total = 0
    for c, num in bags[color].items():
        total += num + num * total_bags(c, bags)
    return total

print(total_bags("shiny gold", bags))