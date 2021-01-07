import re
import itertools

paths = []
for l in open("input.txt"):
    paths.append(re.findall("e|se|sw|w|nw|ne", l))

black = set()
for p in paths:
    coord = [0, 0]

    for d in p:
        if d == "e":
            coord[0] += 1
        elif d == "se":
            coord[0] = coord[0]+1 if coord[1] % 2 == 1 else coord[0]
            coord[1] -= 1
        elif d == "sw":
            coord[0] = coord[0]-1 if coord[1] % 2 == 0 else coord[0]
            coord[1] -= 1
        elif d == "w":
            coord[0] -= 1
        elif d == "nw":
            coord[0] = coord[0]-1 if coord[1] % 2 == 0 else coord[0]
            coord[1] += 1
        elif d == "ne":
            coord[0] = coord[0]+1 if coord[1] % 2 == 1 else coord[0]
            coord[1] += 1
        else:
            assert False

    coord = tuple(coord)
    if coord in black:
        black.remove(coord)
    else:
        black.add(coord)

print(len(black))

def neighbors(c):
    return [
        (c[0] + 1, c[1]),
        (c[0]+1 if c[1] % 2 == 1 else c[0], c[1] - 1),
        (c[0]-1 if c[1] % 2 == 0 else c[0], c[1] - 1),
        (c[0] - 1, c[1]),
        (c[0]-1 if c[1] % 2 == 0 else c[0], c[1] + 1),
        (c[0]+1 if c[1] % 2 == 1 else c[0], c[1] + 1)
    ]

print("="*10, "p2")
for _ in range(100):
    new_black = set()
    minx = min([x for x,y in black])
    maxx = max([x for x,y in black])
    miny = min([y for x,y in black])
    maxy = max([y for x,y in black])

    for c in itertools.product(range(minx-1, maxx+2), range(miny-1, maxy+2)):
        if c in black:
            num_black_neighbors = sum([1 for nc in neighbors(c) if nc in black])
            if 0 < num_black_neighbors <= 2:
                new_black.add(c)
        else:
            num_black_neighbors = sum([1 for nc in neighbors(c) if nc in black])
            if num_black_neighbors == 2:
                new_black.add(c)

    black = new_black

print(len(black))
