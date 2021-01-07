with open("input.txt") as f:
    ETA = int(f.readline())
    busses = [(offset, int(id)) for offset, id in enumerate(f.readline().strip().split(",")) if id.isnumeric()]

buss, wait = min([(b,((ETA // b+1) * b - ETA)) for _, b in busses], key=lambda e: e[1])
print(buss*wait)

t = step = 1
for o, b in busses:
    while (t+o) % b > 0:
        t += step
    step *= b
print(t)
