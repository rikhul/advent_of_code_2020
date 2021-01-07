import collections

p1 = collections.deque()
p2 = collections.deque()

p = p1
for l in open("input.txt"):
    if l.startswith("Player"):
        continue
    
    if not l.strip():
        p = p2
        continue

    p.appendleft(int(l.strip()))


def combat(p1, p2):
    while p1 and p2:
        p1_card, p2_card = p1.pop(), p2.pop()
        if p1_card > p2_card:
            p1.appendleft(p1_card)
            p1.appendleft(p2_card)
        else:
            p2.appendleft(p2_card)
            p2.appendleft(p1_card)
    return p1, p2


def part1(p1, p2):
    p1, p2 = combat(p1, p2)
    winner = p1 if p1 else p2
    score = sum([(value+1)*card for value, card in enumerate(winner)])
    print(score)

part1(p1.copy(),p2.copy())


def rec_combat(p1, p2, rounds):
    while p1 and p2:
        r = (tuple(p1), tuple(p2))
        if r in rounds:
            p2.clear()
            assert p1 and not p2
            return p1, p2
        rounds.add(r)

        p1_card, p2_card = p1.pop(), p2.pop()
        if len(p1) >= p1_card and len(p2) >= p2_card:
            # subgame!
            sub_p1, sub_p2 = collections.deque(list(p1)[-p1_card:]), collections.deque(list(p2)[-p2_card:])
            sub_p1, sub_p2 = rec_combat(sub_p1, sub_p2, set())
            assert not (sub_p1 and sub_p2)
            if sub_p1:
                p1.appendleft(p1_card)
                p1.appendleft(p2_card)
            else:
                p2.appendleft(p2_card)
                p2.appendleft(p1_card)
        elif p1_card > p2_card:
            p1.appendleft(p1_card)
            p1.appendleft(p2_card)
        else:
            p2.appendleft(p2_card)
            p2.appendleft(p1_card)

    return p1, p2

def part2(p1, p2):
    s = len(p1) + len(p2)
    p1, p2 = rec_combat(p1, p2, set())
    winner = p1 if p1 else p2
    assert len(winner) == s
    score = sum([(value+1)*card for value, card in enumerate(winner)])
    print(score)

part2(p1,p2)