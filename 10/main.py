import itertools

adapters = [0]
for l in open("input.txt"):
    adapters.append(int(l))

adapters.sort()
diffs = []
for i, a in enumerate(adapters[1:]):
    diffs.append(a-adapters[i])
diffs.append(3)

numdiff1 = sum([1 for i in diffs if i == 1])
numdiff3 = sum([1 for i in diffs if i == 3])

print(numdiff1*numdiff3)

runs = [len(list(seq))-1 for (d, seq) in itertools.groupby(diffs) if d == 1]
combs = 1
for r in runs:
    combs *= min(2**r, 7)

print(combs)