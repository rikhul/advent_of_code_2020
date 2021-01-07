rules = {}
data = []

for l in open("input.txt"):
    if ":" in l:
        l = l.replace("\"", "")
        i, r = l.strip().split(": ")
        or_rules = [sr.split(" ") for sr in r.split(" | ")]
        rules[str(i)] = or_rules
    elif l.strip():
        data.append(l.strip())

def unroll(r):
    if isinstance(r, list):
        unrolled = [unroll(rr) for rr in r]
        return unrolled
    elif r.isnumeric():
        u = unroll(rules[r])
        return u
    else:
        return r

def match(m, r):
    for or_rule in r:
        all_true = True
        and_idx = 0
        for and_rule in or_rule:
            if isinstance(and_rule, str):
                if m[and_idx] == and_rule:
                    # match
                    and_idx += 1
                else:
                    all_true = False
                    break
            else:
                submatch = match(m[and_idx:], and_rule)
                if submatch:
                    and_idx += submatch
                else:
                    all_true = False
                    break
        if all_true:
            return and_idx

    return 0

def p1():
    r0 = unroll(rules['0'])
    matches = 0
    for msg in data:
        if len(msg) == match(msg, r0):
            matches += 1
    print(matches)


def match_8(m):
    idx = 0
    matches = []
    
    while True:
        matchlen = match_w_lookup(m[idx:], '42')
        if matchlen > 0:
            idx += matchlen
            matches.append(idx)
        else:
            break
    return matches


def match_11(m):
    idx = 0
    match_balance = 0
    while True:
        matchlen = match_w_lookup(m[idx:], '42')
        if matchlen > 0:
            match_balance += 1
            idx += matchlen
        else:
            break
    if not idx:
        return 0
    while True:
        matchlen = match_w_lookup(m[idx:], '31')
        if matchlen > 0:
            match_balance -= 1
            idx += matchlen
            if idx == len(m):
                break
        else:
            break
    if match_balance == 0 and idx == len(m):
        return idx
    else:
        return 0


def match_w_lookup(m, ridx):
    r = rules[ridx]
    idx = 0
    for or_rule in r:
        for and_rule in or_rule:
            if idx == len(m):
                idx = 0
                break
            if and_rule.isnumeric():
                if and_rule == '8':
                    matchlen = match_8(m[idx:])
                elif and_rule == '11':
                    matchlen = match_11(m[idx:])
                else:
                    matchlen = match_w_lookup(m[idx:], and_rule)
                if matchlen > 0:
                    idx += matchlen
                else:
                    idx = 0
                    break
            else:
                if m[idx] == and_rule:
                    idx += 1
                else:
                    idx = 0
                    break
        if idx > 0:
            break
    return idx


def rule0p2(msg):
    idx_42 = match_8(msg)

    for idx in idx_42:
        if match_11(msg[idx:]):
            return True

    return False

def p3():
    matches = []
    no_matches = []
    for msg in data:
        if rule0p2(msg):
            matches.append(msg)
        else:
            no_matches.append(msg)
        
    print(len(matches))

#p1()
p3()