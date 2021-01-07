rows = [l.strip() for l in open("input.txt")]

def num_trees(slope):
    pos = (0,0)
    tree_count = 0
    while pos[1] < len(rows):
        if rows[pos[1]][pos[0]] == '#':
            tree_count += 1
        pos = ((pos[0]+slope[0]) % len(rows[0]), pos[1]+slope[1])
    return tree_count

print(num_trees((3,1)))

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
hits = [num_trees(s) for s in slopes]

prod = 1
for h in hits:
    prod *= h
print(prod)