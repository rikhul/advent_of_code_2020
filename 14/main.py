def program():
    for l in open("input.txt"):
        if "mask" in l:
            yield "mask", l.strip().replace("mask = ", "")
        else:
            addr, val = l.strip().replace("mem[","").replace("] = ", ",").split(",")
            addr, val = int(addr), int(val)
            yield "ins", addr, val


def p1():
    mask = ""
    memory = dict()
    for instruction, *args in program():
        if instruction == "mask":
            mask = args[0]
        else:
            addr, val = args
            masked_val = "".join([v if m == "X" else m for m,v in zip(mask, f'{val:b}'.zfill(len(mask)))])
            memory[addr] = int(masked_val, 2)

    print(sum(memory.values()))


def addresses(masked_address):
    if not masked_address:
        return [""]
    res = []
    for i in range(len(masked_address)):
            for a in addresses(masked_address[i+1:]):
                if masked_address[i] == "X":
                    res.append(masked_address[:i] + "0" + a)
                    res.append(masked_address[:i] + "1" + a)
                else:
                    res.append(masked_address[:i+1] + a)
            return res
    return res


def p2():
    memory = {}
    mask = ""
    for instruction, *args in program():
        if instruction == "mask":
            mask = args[0]
        else:
            addr, val = args
            masked_addr = "".join([a if m == "0" else m for m,a in zip(mask, f'{addr:b}'.zfill(len(mask)))])
            addrs = [int(a,2) for a in addresses(masked_addr)]
            for a in addrs:
                memory[a] = val
    print(sum(memory.values()))


p1()
p2()