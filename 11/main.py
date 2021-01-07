area = ""
for l in open("input.txt"):
    cols = len(l.strip())
    area += l.strip()
rows = len(area) / cols


def step(x, y, dx, dy):
    while 0 <= x+dx < cols and 0 <= y+dy < rows:
        yield x+dx + (y+dy)*cols
        x += dx
        y += dy

directions = (
    (-1,-1), (0,-1), (1,-1),
    (-1, 0),         (1, 0), 
    (-1, 1), (0, 1), (1, 1)
)

def p1(a, n_limit=4, line_of_sight=False):
    while True:
        new_area = []
        for p in range(len(a)):
            x = p % cols
            y = p // cols
            ns = []
            for d in directions:
                for n in step(x, y, d[0], d[1]):
                    if line_of_sight and a[n] == ".":
                        continue
                    ns.append(a[n])
                    break

            if a[p] == "L" and ns.count("#") == 0:
                new_area.append("#")
            elif a[p] == "#" and ns.count("#") >= n_limit:
                new_area.append("L")
            else:
                new_area.append(a[p])
        
        new_area_s = "".join(new_area)
        if a == new_area_s:
            break
        a = new_area_s

    return a.count("#")


#print(p1(area), p1(area,5,True))
print(p1(area))