import math

def binary_search(sequence):
    lower, upper = 0, 2**len(sequence)-1
    for c in sequence:
        if c in "FL":
            upper = lower + math.floor((upper-lower)/2)
        else:
            lower = lower + math.ceil((upper-lower)/2)
    return lower


sids = []
for code in open("input.txt"):
    row = binary_search(code[:7])
    col = binary_search(code[7:10])
    sids.append(row*8+col)

print(max(sids))

for sid in range(1, 127*8):
    if sid not in sids and sid-1 in sids and sid+1 in sids:
        print(sid)
        break
