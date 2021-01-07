for l in open("test_input.txt"):
    seq = [int(n) for n in l.split(",")]

def p1(n=2020):
    turns_reverse_index = dict([(n,i) for i,n in enumerate(seq)])
    last_spoken = 0
    for turn in range(len(turns_reverse_index), n-1):
        diff = turn - turns_reverse_index.get(last_spoken, turn)
        turns_reverse_index[last_spoken] = turn
        last_spoken = diff
    return last_spoken


print(p1())
print(p1(30000000))