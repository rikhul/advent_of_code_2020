import math
import itertools


def coords2(gen, size, dim):
    return itertools.product(*[range(-1-gen, size+1+gen) for _ in range(dim)])


def neighbors2(c):
    all_neighbors = itertools.product(*[range(i-1, i+2) for i in c])
    return filter(lambda n: n !=c, all_neighbors)


def p2(dim=3):
    pocket = "".join([l.strip() for l in open("input.txt").readlines()])
    grid = int(math.sqrt(len(pocket)))
    active = set()
    for y in range(grid):
        for x in range(grid):
            if pocket[y*grid+x] == "#":
                active.add((x,y) + tuple([0]*(dim-2)))

    for gen in range(6):
        new_active = set()
        for c in coords2(gen, grid, dim):
            num_active_neigbors = sum([1 for n in neighbors2(c) if n in active])
            if c in active:
                if num_active_neigbors in (2,3):
                    new_active.add(c)
            elif num_active_neigbors == 3:
                new_active.add(c)
        active = new_active
    
    print(len(active))


p2(3)
p2(4)
