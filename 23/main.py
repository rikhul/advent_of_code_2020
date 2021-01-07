import time

def game(data, rounds=100):
    current = 0
    current_v = data[0]

    for _ in range(rounds):
        dest_target_val = data[current]-1 or 9
        
        l,r = (current+1) % len(data), (current+4) % len(data)
        if r < l:
            pickup = data[l:] + data[:r]
            data = data[r:l]
        else:
            pickup = data[l:r]
            data = data[:l] + data[r:]

        while dest_target_val in pickup:
            dest_target_val = dest_target_val-1 or 9
        target = data.index(dest_target_val)

        data = data[:target+1] + pickup + data[target+1:]

        current = (data.index(current_v)+1)%len(data)
        current_v = data[current]
    return data


def p1():
    data = [int(d) for d in "389125467"]
    data = game(data, 10**2)
    idx = data.index(1)+1
    res = "".join([str(data[(idx+i)%9]) for i in range(8)])
    print(res)
    #assert res == "92658374"
    assert res == "67384529"


p1()


def game2(data, rounds=100):
    next_i = [0]*len(data)

    for i,n in enumerate(data):
        next_i[n-1] = (i+1) % len(data)

    current = data[0]
    for _ in range(rounds):
        pickup = []
        p_idx = next_i[current-1]
        for _ in range(3):
            pickup.append(data[p_idx])
            p_idx = next_i[data[p_idx]-1]
        
        target = current-1 or len(data)
        while target in pickup:
            target = target-1 or len(data)

        target_next_copy = next_i[target-1]
        next_i[target-1] = next_i[current-1]
        next_i[current-1] = next_i[pickup[-1]-1]
        next_i[pickup[-1]-1] = target_next_copy

        current = data[next_i[current-1]]

    return [data[next_i[0]], data[next_i[data[next_i[0]]-1]]]


def p2():
    data = [int(d) for d in "219347865"] + list(range(10, 10**6+1))
    assert len(data) == 10**6
    data = game2(data, 10**7)
    print(data[0]*data[1])
    #assert res == "92658374"
    #assert res == "67384529"

p2()
