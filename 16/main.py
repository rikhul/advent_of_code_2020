import re

def rules():
    with open("input.txt") as f:
        p = re.compile(r"(.+?): (\d+)-(\d+) or (\d+)-(\d+)")
        while True:
            line = f.readline().strip()
            if not line:
                return
            fn, l1, u1, l2, u2 = p.match(line).groups()
            yield fn, int(l1), int(u1), int(l2), int(u2)


def tickets():
    with open("input.txt") as f:
        while True:
            if f.readline().strip() == "nearby tickets:":
                break

        for line in f:
            yield [int(field) for field in line.strip().split(",")]


def your_ticket():
    with open("input.txt") as f:
        while True:
            if f.readline().strip() == "your ticket:":
                break
        line = f.readline().strip()
        yield [int(field) for field in line.strip().split(",")]


def compliant(field, rule):
    _, l1,u1,l2,u2 = rule
    return l1 <= field <= u1 or l2 <= field <= u2


def p1():
    rs = [r for r in rules()]
    ts = [t for t in tickets()]

    non_compliant = []
    for ticket in ts:
        for field in ticket:
            if not any([compliant(field, rule) for rule in rs]):
                non_compliant.append(field)

    print(sum(non_compliant))

def p2():
    rs = [r for r in rules()]
    ts = [t for t in tickets()]
    my_ticket = next(your_ticket())

    valid_tickets = [my_ticket]
    for ticket in ts:
        valid_fields = [any([compliant(field, rule) for rule in rs]) for field in ticket]
        if all(valid_fields):
            valid_tickets.append(ticket)

    # pivot
    columns = [[] for _ in my_ticket]
    for t in valid_tickets:
        for i, c in enumerate(t):
            columns[i].append(c)

    possible_columns = {}
    for i, c in enumerate(columns):
        for r in rs:
            c_compliant = all([compliant(f, r) for f in c])
            if c_compliant:
                if not possible_columns.get(r[0]):
                    possible_columns[r[0]] = set([i])
                else:
                    possible_columns[r[0]].add(i)

    # elimenate
    while not all([len(cs) == 1 for cs in possible_columns.values()]):
        for r, cs in possible_columns.items():
            if len(cs) == 1:
                locked_column = list(cs)[0]
                for r2, cs2 in possible_columns.items():
                    if r == r2:
                        continue
                    if locked_column in cs2:
                        cs2.remove(locked_column)

    # departure columns
    dep_columns = [i for f,i in possible_columns.items() if f.startswith("departure")]

    dep_columns_hash = 1
    for dep_c in dep_columns:
        dep_columns_hash *= my_ticket[list(dep_c)[0]]
    
    print(dep_columns_hash)

p1()
p2()
