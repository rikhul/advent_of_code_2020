import re

p = re.compile(r"[\+\*]|\d+|[\(\)]")

def parse(exp):
    exp = exp.replace(" ", "").strip()
    return [int(t) if t.isnumeric() else t for t in p.findall(exp)]

def calc(exp, level=0):
    left = []
    for t in exp:
        print(" "*level, "t", t)
        if t == "*":
            leftres = calc(left, level+1)
            right = calc(exp, level+1)
            res =  leftres * right
            print(leftres, "*", right, "=", res)
            return res
        elif t == "+":
            lft = calc(left, level+1)
            right = calc(exp, level+1)
            res = lft + right
            print(left, "+", right, "=", res)
            return res
        elif t == "(":
            for inner in exp:
                if inner == ")":
                    return calc(left, level+1)
                left.append(inner)
            return calc(exp, level+1)
        else:
            left.append(int(t))
    print(left[0])
    return left[0]

ops = {
    "+": lambda x,y: x+y,
    "*": lambda x,y: x*y
}

def calc2(exp):
    val = None
    op = None
    for t in exp:
        if t.isnumeric():
            if op:
                val = ops[op](val, int(t))
            else:
                val = int(t)
        elif t in "+*":
            op = t
        elif t == "(":
            res = calc2(exp)
            if op:
                val = ops[op](val, res)
            else:
                val = res
        elif t == ")":
            return val
    return val


def calc3(exp, x=False):
    seq = []
    for t in exp:
        if t.isnumeric():
            seq.append([int(t)])
            if x:
                return seq
        elif t == "+":
            seq = [["+"] + seq + calc3(exp)]
        elif t == "*":
            seq = [["*"] + seq + calc3(exp)]
        elif t == ")":
            return calc3(exp)
        elif t == "(":
            #print("end", seq)
            return seq
    #print("return", seq)
    return seq


def calc4(exp):
    while "(" in exp:
        start = end = exp.index("(")+1
        level = 1
        for i, t in enumerate(exp[start:]):
            if t == "(":
                level += 1
            if t == ")":
                level -= 1
            if level == 0:
                end = i+start
                break
        exp = exp[:start-1] + calc4(exp[start:end]) + exp[end+1:]
    while "+" in exp:
        for i, t in enumerate(exp):
            if t == "+":
                s = exp[i-1] + exp[i+1]
                exp = exp[:i-1] + [s] + exp[i+2:]
                break
    while "*" in exp:
        for i, t in enumerate(exp):
            if t == "*":
                s = exp[i-1] * exp[i+1]
                exp = exp[:i-1] + [s] + exp[i+2:]
                break
    return exp


s = 0
for l in open("input.txt"):
    s += calc4(parse(l))[0]
    
print(s)
