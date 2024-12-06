from fileinput import input
import re

lines = [line for line in input()]

line = ''.join(l.strip() for l in lines)

linelen = len(lines[0].strip())

class Board:
    def __init__(self, line, w):
        self.line = line
        self.w = w

    def in_bounds(self, pos):
        if isinstance(pos, int):
            return pos in range(0, len(self.line)) 
        x,y = pos
        return x >= 0 and y >= 0 and x < self.w and y < (len(self.line) // self.w)

    def get(self, pos):
        i = pos if isinstance(pos, int) else self.coordtoi(pos)
        return line[i] if self.in_bounds(i) else None

    def add(self, pos, d):
        coords = self.itocoord(pos) if isinstance(pos, int) else pos
        res = tuple(map(sum, zip(d, coords)))
        return self.coordtoi(res) if isinstance(pos, int) else res

    def coordtoi(self, pos):
        x,y = pos
        return y*self.w+x

    def itocoord(self, i):
        return i % self.w, int(i / self.w)


board = Board(line, linelen)

dirs = [(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1),(0,1),(0,-1)]
mdirs = [(1,1),(1,-1),(-1,1),(-1,-1)]

def is_xmas(word, d, let, pos):
    if let == len(word):
        return True

    if board.get(pos) != word[let] or not board.in_bounds(pos):
        return False

    return is_xmas(word, d, let+1, board.add(pos,d))

def check_dirs(x, dirs, pos):
    coords = board.itocoord(pos)
    return [is_xmas(x, d, 0, coords) for d in dirs]

def get_as(x, dirs, pos):
    coords = board.itocoord(pos)
    return [board.add(coords,d) for d in dirs if is_xmas(x, d, 0, coords)]

def find_locs(line, char):
    return [d for d,_ in filter(lambda c: c[1] == char, enumerate(line))]

total = sum(map(lambda pos: sum(check_dirs("XMAS", dirs, pos)), find_locs(line, "X"))) 
print("part 1",total)

ass = sum(map(lambda pos: get_as("MAS", mdirs, pos), find_locs(line, "M")),[])
total2 = len(ass) - len(set(ass))
print("part 2", total2)
