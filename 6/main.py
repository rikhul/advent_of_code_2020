group = []
groups = []

for l in open("input.txt"):
    l = l.strip()
    if not l:
        groups.append(group)
        group = []
    else:
        group.append(l)
groups.append(group)

unions = []
commons = []
for g in groups:
    union_g = set()
    common_g = set(g[0])
    for i in g:
        union_g = union_g.union(i)
        common_g = common_g.intersection(i)
    unions.append(union_g)
    commons.append(common_g)

print(sum([len(u) for u in unions]))
print(sum([len(u) for u in commons]))
