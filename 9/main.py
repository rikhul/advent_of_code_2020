import collections
import itertools


def input():
    for l in open("input.txt"):
        yield int(l)


def possible_sum(s, candidates):
    for i, n in enumerate(candidates[:-1]):
        for _, n2 in enumerate(candidates[i+1:]):
            if n+n2 == s:
                return True
    return False


numbers = input()
candidates = list(itertools.islice(numbers, 25))

error_n = 0
for i, n in enumerate(numbers):
    if not possible_sum(n, candidates):
        error_n = n
        break
    candidates[i % len(candidates)] = n

print(error_n)

q = collections.deque()
for n in input():
    if sum(q) == error_n:
        print(min(q) + max(q))
        break

    while sum(q) > error_n:
        q.popleft()

    if sum(q) < error_n:
        q.append(n)
