code = []
for l in open("input"):
    instruction, arg = l.strip().split(" ")
    code.append((instruction, int(arg)))

def run(code):
    ip = 0
    acc = 0
    visited = []
    while True:
        visited.append(ip)
        i, a = code[ip]
        if i == "nop":
            ip += 1
        elif i == "acc":
            acc += a
            ip +=1
        elif i == "jmp":
            ip += a

        if ip in visited or ip == len(code):
            break
    return ip, acc

_, acc = run(code)
print(acc)

for i in range(len(code)):
    ins, arg = code[i]
    if ins == "jmp":
        code[i] = ("nop", arg)
        ip, acc = run(code)
        if ip == len(code):
            print(acc)
            break
        else:
            code[i] = ("jmp", arg)
    if ins == "nop":
        code[i] = ("jmp", arg)
        ip, acc = run(code)
        if ip == len(code):
            print(acc)
            break
        else:
            code[i] = ("nop", arg)
