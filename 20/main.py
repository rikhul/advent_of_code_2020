import math
import re

TOP, RIGHT, BOTTOM, LEFT = range(4)

class Tile():
    def __init__(self, text):
        self.number = ""
        self.data = []
        if text:
            self.number, *self.data = text.strip().split("\n")
            self.number = self.number.replace("Tile ", "").replace(":", "")
            self._update_edges()

    def _update_edges(self):
        self.edges = [self.data[0], "", self.data[-1], ""]
        for r in self.data:
            self.edges[1] += r[-1]
            self.edges[3] += r[0]

    def rotate(self):
        nd = ["" for _ in range(len(self.data))]
        for x in range(len(self.data)):
            for y in range(len(self.data)-1, -1,-1):
                nd[x] += self.data[y][x]
        self.data = nd
        self._update_edges()

    def flip(self):
        for i, row in enumerate(self.data):
            self.data[i] = row[::-1]
        self._update_edges()
    
    def inner_data(self):
        for row in self.data[1:-1]:
            yield row[1:-1]
    
    def edge(self, dir):
        return self.edges[dir]

    def __repr__(self):
        return self.number


def candidate_spots(grid, size):
    miny = min([y for x,y in grid])
    minx = min([x for x,y in grid])
    y = miny
    while True:
        rowlen = len([1 for gx,gy in grid if gy == y])
        if 1 <= rowlen < size:
            return [(minx+rowlen, y), (minx-1 if y == 0 else minx, y)]
        if rowlen == 0:
            return [(minx, y), (minx, miny-1)]
        y += 1

def solve_pussle(grid, tiles, size):
    if not tiles:
        return grid

    for spot in candidate_spots(grid, size):
        for t in tiles:
            if fits(t, spot, grid):
                subgrid = grid.copy()
                subgrid[(spot)] = t
                subtiles = tiles.copy()
                subtiles.remove(t)
                resgrid = solve_pussle(subgrid, subtiles, size)
                if len(resgrid) == size**2:
                    return resgrid
    return grid

def neighbors(spot, grid):
    return [grid.get((spot[0]+d[0], spot[1]+d[1]), None) for d in ((-1, 0), (1, 0), (0,-1), (0,1))]


def fits(t, spot, grid):
    left, right, top, bottom = neighbors(spot, grid)
    num_neighbors = sum([1 for n in (left, right, bottom, top) if n])

    for _ in range(2):
        for _ in range(4):
            num_match = 0
            if left:
                num_match += 1 if left.edge(RIGHT) == t.edge(LEFT) else 0
            if right:
                num_match += 1 if right.edge(LEFT) == t.edge(RIGHT) else 0
            if bottom:
                num_match += 1 if bottom.edge(TOP) == t.edge(BOTTOM) else 0
            if top:
                num_match += 1 if top.edge(BOTTOM) == t.edge(TOP) else 0
            if num_match == num_neighbors:
                return True
            t.rotate()
        else:
            t.flip()
    return False


def p1(tiles):
    gridsize = int(math.sqrt(len(tiles)))
    grid = {
        (0,0): tiles[0],
    }
    tiles = tiles[1:]
    grid = solve_pussle(grid, tiles, gridsize)

    miny = min([y for x,y in grid.keys()])
    minx = min([x for x,y in grid.keys()])

    corners = (
        (minx, miny),
        (minx, miny+gridsize-1),
        (minx+gridsize-1, miny),
        (minx+gridsize-1,miny+gridsize-1)
    )

    p = 1
    for tile in [grid[p] for p in corners]:
        p *= int(tile.number)
    print("p1", p)
    assert p == 64802175715999 or p == 20899048083289
    return grid


def p2(grid):
    grid_size = int(math.sqrt(len(grid)))
    tile_size = len(next(grid[(0,0)].inner_data()))

    picture_rows = ['' for _ in range(grid_size*tile_size)]

    miny = min([y for x,y in grid.keys()])
    minx = min([x for x,y in grid.keys()])

    # here I used only y first, but that will insert into picture_rows[-5] or whatever instead of 0
    # hence very deceptively scrampling the picture because monsters mostly stay intact
    for iy, y in enumerate(range(miny,miny+grid_size)):
        for x in range(minx, minx+grid_size):
            for i, data_row in enumerate(grid[(x,y)].inner_data()):
                picture_rows[iy*tile_size+i] += data_row

    # put picture in a tile to be able to rotate n flip it
    picture = Tile("")
    picture.data = picture_rows

    monster = (
        "..................#.",
        "#....##....##....###",
        ".#..#..#..#..#..#...",
    )

    # pad monster
    bigmonster = ("."*(len(picture.data)-len(monster[0]))).join(monster)
    # add regex magic to find overlapping monsters
    bigmonster = "(?=(" + bigmonster + "))"

    # flip n rotate picture until we find any monster
    for _ in range(2):
        for _ in range(4):
            bigsea = "".join(picture.data)
            monsters = list(re.finditer(bigmonster, bigsea))
            if monsters:
                break
            picture.rotate()
        if monsters:
            break
        picture.flip()

    # not necessary, could just do bigsea.count("#")-len(monsters)*bigmonster.count("#")
    # but nice for debugging
    bigsea = list(bigsea)
    for m in monsters:
        monster_sea = bigsea[m.start(1):m.end(1)]
        highlight = "".join(["O" if m == "#" else s for m,s in zip(bigmonster[4:-2], monster_sea)])
        bigsea[m.start(1):m.end(1)] = highlight
  
    assert bigsea.count("#") == 2146
    print("p2", bigsea.count("#"), "water roughness")


tiles = []
tile_data = ""
for l in open("input.txt"):
    if not l.strip():
        tiles.append(Tile(tile_data))
        tile_data = ""
    elif l.strip():
        tile_data += l
if tile_data:
    tiles.append(Tile(tile_data))
    tile_data = ""

grid = p1(tiles)
p2(grid)
