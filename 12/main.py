def input():
    for l in open("input.txt"):
        i = l.strip()
        yield i[:1], int(i[1:])


class Coordinate():
    x,y = 0,0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, deg):
        for _ in range(deg//90):
            self.x, self.y = self.y, -self.x


def p1(move_wp=False):
    boat = Coordinate(0, 0)
    wp = Coordinate(10, 1) if move_wp else Coordinate(1, 0)
    to_move = wp if move_wp else boat
    for ins, val in input():
        if ins == "N":
            to_move.y += val
        elif ins == "S":
            to_move.y -= val
        elif ins == "E":
            to_move.x += val
        elif ins == "W":
            to_move.x -= val
        elif ins in "LR":
            if ins == "L":
                val = 360-val
            wp.rotate(val)
        elif ins == "F":
            boat.x += wp.x * val
            boat.y += wp.y * val

    print(abs(boat.x)+abs(boat.y))

p1()
p1(True)